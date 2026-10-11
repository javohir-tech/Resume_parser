import asyncio
import io
import unittest

from pypdf import PdfReader
from app.services.resume_pdf import create_resume_pdf, _restricted_html


class ResumePdfTests(unittest.TestCase):
    def test_untrusted_document_is_restricted(self):
        result = _restricted_html('<html><head><base href="http://localhost"><meta http-equiv="refresh" content="0;url=http://localhost"></head><body onload="alert(1)"><script>alert(1)</script><iframe src="http://localhost"></iframe><p>Resume</p></body></html>')
        self.assertNotIn('<script', result)
        self.assertNotIn('<iframe', result)
        self.assertNotIn('onload=', result)
        self.assertIn("default-src 'none'", result)

    def test_pdf_from_selector_loop(self):
        html = '''<html><head><style>
        @page { size: A4; margin: 0 }
        body { margin: 0 }
        section { height: 297mm; break-after: page }
        section:last-child { break-after: auto }
        </style></head><body><section>First resume page</section>
        <section>Second resume page</section></body></html>'''
        with asyncio.Runner(loop_factory=asyncio.SelectorEventLoop) as runner:
            pdf = runner.run(create_resume_pdf(html))
        self.assertTrue(pdf.startswith(b'%PDF-'))
        reader = PdfReader(io.BytesIO(pdf))
        self.assertEqual(len(reader.pages), 2)
        self.assertIn('First resume page', reader.pages[0].extract_text())
        self.assertIn('Second resume page', reader.pages[1].extract_text())


if __name__ == '__main__':
    unittest.main()
