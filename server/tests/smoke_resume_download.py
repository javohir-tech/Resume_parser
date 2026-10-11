"""Integration smoke: actual Vue templates -> HTML snapshot -> PDF (no DB writes)."""
import io
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from app.services.resume_pdf import _render_pdf

ROOT = Path(__file__).resolve().parents[2]
source = ROOT / 'client/app/features/resume/download-resume/models/buildResumeHtml.ts'
compiled = subprocess.check_output(['node', '-e', '''
const fs = require('node:fs');
const {stripTypeScriptTypes} = require('node:module');
let source = fs.readFileSync(process.argv[1], 'utf8');
source = source.replace('import { nextTick } from "vue";', 'const nextTick = () => Promise.resolve();');
source = source.replace('export async function buildResumeHtml', 'async function buildResumeHtml');
process.stdout.write(stripTypeScriptTypes(source) + '\\nwindow.buildResumeHtml = buildResumeHtml;');
''', str(source)], text=True)

resume = dict(id='pdf-smoke', fullname='PDF Test User', title='Frontend Developer', email='test@example.com', phone='', location='Tashkent', website='', github_link='', linkedin_link='', summary='Resume export verification.', education=[], experience=[], skills=[], languages=[])
resume['experience'] = [dict(id=str(i), position=f'Engineer {i}', company='Example Company', location='Tashkent', startDate='2020', endDate='2024', description='Built accessible interfaces and reliable services. ' * 8) for i in range(10)]
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    try:
        for template in ([] if '--button-only' in sys.argv else ['classic', 'modern', 'minimal', 'professional', 'sidebar']):
            page = browser.new_page()
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            def handle(route):
                data = dict(template=template, font='Inter', heading_title_color='#10b981', entry_title_color='#10b981') if route.request.url.endswith('/design') else resume
                route.fulfill(json=data, headers={'Access-Control-Allow-Origin': '*'})
            page.route('http://localhost:8000/api/resume/**', handle)
            page.goto('http://localhost:3000/resume/pdf-smoke/view', wait_until='networkidle', timeout=90000)
            page.wait_for_selector('[data-pdf-page]', timeout=30000)
            page.add_script_tag(content=compiled)
            html = page.evaluate('() => window.buildResumeHtml()')
            expected_pages = page.locator('[data-pdf-page]').count()
            with ThreadPoolExecutor(max_workers=1) as executor:
                pdf = executor.submit(_render_pdf, html).result()
            reader = PdfReader(io.BytesIO(pdf))
            assert len(reader.pages) == expected_pages, (template, len(reader.pages), expected_pages)
            text = ' '.join(''.join(p.extract_text() for p in reader.pages).lower().split())
            assert 'pdf test user' in text, (template, text[:500])
            assert 'engineer 9' in text, (template, text[-500:])
            assert not errors, errors
            print(template, 'OK', expected_pages, 'pages', len(html), 'HTML chars', flush=True)
            page.close()
        # Exercise the real button/composable with an isolated fake session.
        page = browser.new_page()
        page.context.add_cookies([dict(name='access_token', value='pdf-test-only', url='http://localhost:3000')])
        page.route('**/api/users/me', lambda route: route.fulfill(json=dict(id='test', full_name='Test', username=None, telegram_id=0, registered_at='2026-01-01')))
        def editor_api(route):
            if route.request.method == 'OPTIONS':
                route.fulfill(status=204, headers={'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': 'POST, GET, PATCH'})
            elif route.request.url.endswith('/download'):
                assert route.request.method == 'POST'
                html = route.request.post_data_json['html']
                with ThreadPoolExecutor(max_workers=1) as executor:
                    pdf = executor.submit(_render_pdf, html).result()
                route.fulfill(body=pdf, content_type='application/pdf', headers={'Access-Control-Allow-Origin': '*'})
            elif route.request.url.endswith('/design'):
                route.fulfill(json=dict(template='classic', font='Inter', heading_title_color=None, entry_title_color=None), headers={'Access-Control-Allow-Origin': '*'})
            else:
                route.fulfill(json=resume, headers={'Access-Control-Allow-Origin': '*'})
        page.route('http://localhost:8000/api/resume/**', editor_api)
        page.goto('http://localhost:3000/resume/pdf-smoke', wait_until='networkidle')
        page.wait_for_selector('[data-pdf-page]')
        with page.expect_download(timeout=60000) as result:
            page.get_by_role('button', name='Download', exact=True).click()
        download = result.value
        assert download.suggested_filename == 'resume-pdf-smoke.pdf'
        assert download.failure() is None
        assert page.url.endswith('/resume/pdf-smoke')
        print('Download button OK: file received without navigation', flush=True)
        page.close()
    finally:
        browser.close()
