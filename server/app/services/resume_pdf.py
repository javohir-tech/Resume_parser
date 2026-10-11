"""Print self-contained HTML in a worker thread (also supports Windows reload)."""
import asyncio
from threading import BoundedSemaphore

from lxml import etree, html as html_parser
from playwright.sync_api import sync_playwright
from app.core.config import settings

_pdf_slots = BoundedSemaphore(2)


def _restricted_html(html: str) -> str:
    document = html_parser.document_fromstring(html)
    for node in document.xpath('//script|//iframe|//frame|//object|//embed|//base|//link|//meta'):
        node.drop_tree()
    for node in document.iter():
        for attribute in list(node.attrib):
            if attribute.lower().startswith('on'):
                del node.attrib[attribute]
    head = document.find('head')
    if head is None:
        head = etree.Element('head')
        document.insert(0, head)
    policy = etree.Element('meta', attrib={
        'http-equiv': 'Content-Security-Policy',
        'content': "default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; base-uri 'none'; form-action 'none'",
    })
    head.insert(0, policy)
    return html_parser.tostring(document, encoding='unicode', doctype='<!DOCTYPE html>')


def _render_pdf(html: str) -> bytes:
    if not _pdf_slots.acquire(timeout=settings.PDF_TIMEOUT_SECONDS):
        raise TimeoutError('PDF queue is busy')
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=True, timeout=settings.PDF_TIMEOUT_SECONDS * 1000,
            )
            try:
                context = browser.new_context(java_script_enabled=False, service_workers='block')
                try:
                    context.route('**/*', lambda route: route.abort())
                    page = context.new_page()
                    page.set_default_timeout(settings.PDF_TIMEOUT_SECONDS * 1000)
                    page.emulate_media(media='print')
                    page.set_content(_restricted_html(html), wait_until='load')
                    page.evaluate('() => document.fonts.ready.then(() => true)')
                    return page.pdf(
                        format='A4', print_background=True, prefer_css_page_size=True,
                        margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                    )
                finally:
                    context.close()
            finally:
                browser.close()
    finally:
        _pdf_slots.release()


async def create_resume_pdf(html: str) -> bytes:
    return await asyncio.to_thread(_render_pdf, html)
