import logging
import asyncio


from uuid import UUID
from typing import Literal

from fastapi import APIRouter, Depends, status, Query, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import Response

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from pydantic import UUID4, BaseModel, Field

from fastapi_filter import FilterDepends
from fastapi_filter.contrib.sqlalchemy import Filter


from app.db.session import get_db

from app.core.security import verify

from app.models.resume import Resume
from app.models.skills import Skills
from app.models.user import User
from app.models.design_info import Design

from app.schemas.resume_schemas import PersonalInfo

from app.services.resume_pdf import create_resume_pdf
from app.services.resume_input_hash import build_input_hash


from playwright.async_api import (
    Error as PlaywrightError,
    TimeoutError as PlaywrightTimeoutError,
)

current_router = APIRouter(prefix="/resume", tags=["resume"])


# /////////////////////////////////////////////////////////
# /////////////////  FILTER RESUME  ///////////////////////
# /////////////////////////////////////////////////////////
class ResumeFilter(Filter):
    search: str | None = None

    class Constants(Filter.Constants):
        model = Resume
        search_model_fields = ["fullname", "title", "job_company", "job_title"]


@current_router.get("/")
async def get_my_resumes(
    request: Request,
    filters: ResumeFilter = FilterDepends(ResumeFilter),
    db: AsyncSession = Depends(get_db),
    resume_type: Literal["all", "orginal", "ai"] = "all",
    resume_id: UUID4 | None = None,
    page: int = Query(default=1, ge=1),
    user_id: str = Depends(verify),
):

    page_size = 10

    query = select(Resume).where(Resume.user_id == UUID(user_id))

    if resume_type == "orginal":
        query = query.where(Resume.parent_resume_id.is_(None))
    if resume_type == "ai":
        query = query.where(Resume.parent_resume_id.is_not(None))

    query = filters.filter(query)

    if resume_id is not None:
        query = query.where(Resume.id == resume_id)

    count_query = select(func.count()).select_from(query.order_by(None).subquery())

    total = await db.scalar(count_query) or 0

    query = (
        query.order_by(Resume.created_at.desc(), Resume.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )

    result = await db.execute(query)
    resumes = result.scalars().all()

    def page_url(number: int) -> str:
        return str(request.url.include_query_params(page=number))

    return {
        "count": total,
        "next": page_url(page + 1) if page * page_size < total else None,
        "previous": page_url(page - 1) if page > 1 else None,
        "results": [
            {
                "id": resume.id,
                "fullname": resume.fullname or "",
                "title": resume.title or "",
                "parent_resume_id": resume.parent_resume_id,
                "job_company": resume.job_company,
                "job_title": resume.job_title,
                "cover_letter": resume.cover_letter,
            }
            for resume in resumes
        ],
    }


@current_router.get("/{resume_id}")
async def get_resume(resume_id: str, db: AsyncSession = Depends(get_db)):
    """Return resume data using the frontend field names."""
    resume_uuid = UUID(resume_id)

    result = await db.execute(
        select(Resume)
        .options(
            selectinload(Resume.experience),
            selectinload(Resume.education),
            selectinload(Resume.languages),
            selectinload(Resume.skills).selectinload(Skills.skills),
        )
        .where(Resume.id == resume_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resume Not Found"
        )

    return {
        "id": resume.id,
        "fullname": resume.fullname or "",
        "title": resume.title or "",
        "email": resume.email or "",
        "phone": resume.phone or "",
        "location": resume.location or "",
        "website": resume.website or "",
        "github_link": resume.github_link or "",
        "linkedin_link": resume.linkedin_link or "",
        "summary": resume.summary or "",
        "experience": [
            {
                "id": experience.id,
                "position": experience.position or "",
                "company": experience.company or "",
                "location": experience.location or "",
                "startDate": experience.startDate or "",
                "endDate": experience.endDate or "",
                "description": experience.description or "",
            }
            for experience in resume.experience
        ],
        "education": [
            {
                "id": education.id,
                "degree": education.degree or "",
                "fieldOfStudy": education.fieldOfStudy or "",
                "institution": education.institution or "",
                "location": education.location or "",
                "startDate": education.startDate or "",
                "endDate": education.endDate or "",
            }
            for education in resume.education
        ],
        "languages": [
            {
                "id": language.id,
                "language": language.language or "",
                "degree": language.degree or "",
            }
            for language in resume.languages
        ],
        "skills": [
            {
                "id": skills_group.id,
                "title": skills_group.title or "",
                "skills": [
                    {"id": item.id, "skill": item.skill or ""}
                    for item in skills_group.skills
                ],
            }
            for skills_group in resume.skills
        ],
    }


@current_router.post("/")
async def create_resume(
    db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Create an empty resume for the authenticated user and return its ID."""

    result = await db.execute(select(User).where(User.id == user_id))

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    try:
        resume = Resume(user_id=user.id)
        db.add(resume)

        await db.flush()

        resume_id = resume.id

        design = Design(resume_id=resume_id)
        db.add(design)

        await db.commit()
    except:
        await db.rollback()
        raise

    return {"success": True, "resume_id": resume.id}


@current_router.patch("/{resume_id}")
async def resume_edit(
    resume_id: str,
    personalInfo: PersonalInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Update only the supplied personal information fields in a resume owned by the user."""
    user_uuid = UUID(user_id)
    resume_uuid = UUID(resume_id)

    result = await db.execute(
        select(Resume).where(Resume.id == resume_uuid, Resume.user_id == user_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found among your resumes",
        )

    changes = personalInfo.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(resume, field, value)

    await db.commit()


@current_router.delete("/{resume_id}")
async def delete_resume(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Delete a resume owned by the authenticated user."""
    resume_uuid = UUID(resume_id)
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Resume).where(Resume.id == resume_uuid, Resume.user_id == user_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found among your resumes",
        )

    await db.delete(resume)
    await db.commit()

    return {"success": True, "message": "Resume deleted successfully"}


logger = logging.getLogger(__name__)


class ResumePdfRequest(BaseModel):
    html: str = Field(min_length=1, max_length=15_000_000)


@current_router.post("/{resume_id}/download")
async def download_resume(
    resume_id: UUID,
    payload: ResumePdfRequest,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    result = await db.execute(
        select(Resume).where(Resume.id == resume_id, Resume.user_id == UUID(user_id))
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(status_code=404, detail="Resume topilmadi")

    if resume.user_id != UUID(user_id):
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Ushbu resume sizga tegishli emas",
        )
    try:
        pdf_bytes = await create_resume_pdf(payload.html)
    except (asyncio.TimeoutError, PlaywrightTimeoutError) as error:
        logger.warning("PDF yaratish vaqti tugadi: %s", resume_id)
        raise HTTPException(
            status_code=503,
            detail="PDF yaratib bo'lmadi. Keyinroq qayta urinib ko'ring.",
        ) from error
    except (PlaywrightError, ValueError) as error:
        logger.exception("PDF yaratishda xatolik: %s", resume_id)
        raise HTTPException(
            status_code=503,
            detail="PDF yaratib bo'lmadi. Keyinroq qayta urinib ko'ring.",
        ) from error

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": (f'attachment; filename="resume-{resume_id}.pdf"'),
            "Cache-Control": "no-store",
        },
    )
