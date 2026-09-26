import re
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile, is_zipfile

from docx import Document
from docx.text.paragraph import Paragraph
from fastapi import HTTPException, UploadFile
from pypdf import PdfReader
from starlette.concurrency import run_in_threadpool

from app.core.config import settings


def document_error(status: int, code: str, message: str):
    raise HTTPException(status_code=status, detail={"code": code, "message": message})


def iter_docx_text(container):
    """Paragraflar va ichma-ich jadvallarni tartib bilan o'qiydi"""

    for block in container.iter_inner_content():
        if isinstance(block, Paragraph):
            yield block.text
        else:
            seen_cells = set()

            for row in block.rows:
                for cell in row.cells:
                    if cell._tc in seen_cells:
                        continue
                    seen_cells.add(cell._tc)
                    yield from iter_docx_text(cell)


def read_pdf(data: bytes) -> str:
    if not data.startswith(b"%PDF-"):
        document_error(415, "INVALID_PDF_TYPE", "Fayl haqiqiy PDF emas.")

    reader = PdfReader(BytesIO(data))

    if reader.is_encrypted:
        document_error(422, "ENCRYPTED_PDF", "Parollangan PDF qo'llanmaydi.")

    if len(reader.pages) > settings.MAX_PDF_PAGES:
        document_error(413, "TOO_MANY_PAGES", "PDF sahifalari limitdan oshdi.")

    parts = []
    total = 0

    for page in reader.pages:
        text = page.extract_text() or ""
        total += len(text) + 1

        if total > settings.MAX_TEXT_CHARS:
            document_error(413, "TEXT_TOO_LONG", "Matn limitdan oshdi.")

        parts.append(text)

    return "\n".join(parts)


def read_docx(data: bytes) -> str:
    stream = BytesIO(data)

    if not is_zipfile(stream):
        document_error(415, "INVALID_DOCX_TYPE", "Fayl haqiqiy DOCX emas.")

    with ZipFile(BytesIO(data)) as archive:
        entries = archive.infolist()
        names = {entry.filename for entry in entries}

        required = {
            "[Content_Types].xml",
            "_rels/.rels",
            "word/document.xml",
        }

        if not required.issubset(names):
            document_error(
                415,
                "INVALID_DOCX_TYPE",
                "ZIP ichida Word hujjati topilmadi.",
            )

        if any(entry.flag_bits & 1 for entry in entries):
            document_error(
                422,
                "ENCRYPTED_DOCX",
                "Shifrlangan DOCX qo'llanmaydi.",
            )

        expanded_size = sum(entry.file_size for entry in entries)

        if expanded_size > settings.MAX_DOCX_UNCOMPRESSED_BYTES:
            document_error(
                413,
                "DOCX_TOO_LARGE",
                "DOCX ochilgandagi hajm limitdan oshdi.",
            )

    document = Document(BytesIO(data))
    parts = []
    total = 0

    for text in iter_docx_text(document):
        total += len(text) + 1

        if total > settings.MAX_TEXT_CHARS:
            document_error(413, "TEXT_TOO_LONG", "Matn limitdan oshdi.")

        parts.append(text)

    return "\n".join(parts)


def parse_document(data: bytes, suffix: str) -> str:
    try:
        if suffix == ".pdf":
            text = read_pdf(data)
        else:
            text = read_docx(data)
    except HTTPException:
        raise
    except Exception:
        document_error(
            422,
            "BROKEN_DOCUMENT",
            "Hujjatni o'qib bo'lmadi. Fayl buzilgan bo'lishi mumkin.",
        )

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)
    text = "\n".join(line.strip() for line in text.splitlines())
    text = text.strip()

    if not text:
        document_error(
            422,
            "NO_TEXT",
            "Matn topilmadi. Skanerlangan yoki rasmli hujjat qo'llanmaydi.",
        )

    if len(text) > settings.MAX_TEXT_CHARS:
        document_error(413, "TEXT_TOO_LONG", "Matn limitdan oshdi.")

    return text


async def extract_text(file: UploadFile) -> str:
    suffix = Path(file.filename or "").suffix.lower()

    allowed_mime = {
        ".pdf": {"application/pdf"},
        ".docx": {
            "application/vnd.openxmlformats-officedocument." "wordprocessingml.document"
        },
    }

    try:
        if suffix not in allowed_mime:
            document_error(
                415, "UNSUPPORTED_FORMAT", "Faqat PDF va DOCX yuklash mumkin."
            )

        mime = (file.content_type or "").split(";")[0].lower()

        if mime not in allowed_mime[suffix]:
            document_error(415, "MIME_MISMATCH", "Fayl turi kengaytmasiga mos emas.")

        data = bytearray()

        while True:

            chunk = await file.read(64 * 1024)

            if not chunk:
                break

            if len(data) + len(chunk) > settings.MAX_UPLOAD_BYTES:
                document_error(
                    413,
                    "FILE_TOO_LARGE",
                    "Fayl hajmi limitdan oshdi.",
                )
            data.extend(chunk)

        if not data:
            document_error(422, "EMPTY_FILE", "Fayl bo'sh.")

        return await run_in_threadpool(
            parse_document , bytes(data) , suffix
        )

    finally:
        await file.close()
