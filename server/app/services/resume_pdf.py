import asyncio
import json

from playwright.async_api import async_playwright

from app.core.config import settings


# Har bir server processida ko'pi bilan 2 ta PDF yaratiladi.
_pdf_slots = asyncio.Semaphore(2)


async def _render_pdf(payload: dict) -> bytes:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)

        try:
            context = await browser.new_context(
                viewport={"width": 1280, "height": 900},
                service_workers="block",
            )

            try:
                page = await context.new_page()
                page.set_default_timeout(30_000)

                # Ma'lumotlar frontend JavaScript ishlashidan oldin uzatiladi.
                payload_json = json.dumps(payload, ensure_ascii=True)

                await page.add_init_script(
                    script=(
                        f"window.__RESUME_PDF__ = {payload_json};"
                        "window.__PDF_READY__ = false;"
                    )
                )

                # Sahifalash boshidan print stillari bilan hisoblansin.
                await page.emulate_media(media="print")

                response = await page.goto(
                    settings.PDF_PRINT_URL,
                    wait_until="domcontentloaded",
                    timeout=30_000,
                )

                if response is None or not response.ok:
                    raise RuntimeError("Print sahifasini ochib bo'lmadi")

                # Frontend bu belgini barcha render ishlari tugagach qo'yadi.
                await page.wait_for_function(
                    "window.__PDF_READY__ === true",
                    timeout=30_000,
                )

                await page.evaluate(
                    "() => document.fonts.ready.then(() => true)"
                )

                return await page.pdf(
                    format="A4",
                    print_background=True,
                    prefer_css_page_size=True,
                    margin={
                        "top": "0",
                        "right": "0",
                        "bottom": "0",
                        "left": "0",
                    },
                )
            finally:
                await context.close()
        finally:
            await browser.close()


async def _render_with_limit(payload: dict) -> bytes:
    async with _pdf_slots:
        return await _render_pdf(payload)


async def create_resume_pdf(payload: dict) -> bytes:
    # Navbatda kutish va PDF yaratishga umumiy vaqt chegarasi.
    return await asyncio.wait_for(
        _render_with_limit(payload),
        timeout=settings.PDF_TIMEOUT_SECONDS,
    )