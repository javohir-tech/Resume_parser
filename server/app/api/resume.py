import asyncio
import logging
import json

from uuid import UUID

from typing import Literal

from fastapi import APIRouter, Depends, status, File, UploadFile, Query, Request
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field, UUID4

from sqlalchemy import select, func
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.resume_pdf import create_resume_pdf
from app.services.resume_input_hash import build_input_hash
from app.db.session import get_db
from app.core.security import verify

from app.schemas.resume_schemas import (
    PersonalInfo,
    DesingInfo,
    ResumeJobMatch,
)

from fastapi_filter import FilterDepends
from fastapi_filter.contrib.sqlalchemy import Filter

from app.schemas.resume_parse_schema import ParsedResumeResult, ResumeImportResume

from app.models.user import User
from app.models.resume import Resume
from app.models.experience import Experience
from app.models.educations import Education
from app.models.languages import Language
from app.models.skills import Skills
from app.models.skill_item import SkillItem
from app.models.design_info import Design

from app.services.document_reader import extract_text
from app.services.resume_parser import parse_resume, has_content
from app.services.resume_job_match import job_match_resume

resume_router = APIRouter(prefix="/resume", tags=["Resume"])


@resume_router.post("/parse", response_model=ParsedResumeResult)
async def parse_uploaded_resume(
    file: UploadFile = File(...), user_id: str = Depends(verify)
):
    text = await extract_text(file)
    return await parse_resume(text)


@resume_router.post(
    "/import",
    status_code=status.HTTP_201_CREATED,
)
async def import_parsed_resume(
    payload: ResumeImportResume,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    data = payload.resume

    if not has_content(data.model_dump()):
        raise HTTPException(
            status_code=422,
            detail={
                "code": "EMPTY_RESUME",
                "message": "Bo'sh resume saqlab bo'lmaydi.",
            },
        )

    personal_data = data.model_dump(
        exclude={
            "experience",
            "education",
            "languages",
            "skills",
        }
    )

    resume = Resume(
        user_id=UUID(user_id),
        **personal_data,
    )

    resume.experience = [Experience(**item.model_dump()) for item in data.experience]

    resume.education = [Education(**item.model_dump()) for item in data.education]

    resume.languages = [Language(**item.model_dump()) for item in data.languages]

    resume.skills = [
        Skills(
            title=group.title,
            skills=[SkillItem(skill=item.skill) for item in group.skills],
        )
        for group in data.skills
    ]

    async with db.begin():
        db.add(resume)
        await db.flush()
        resume_id = resume.id

        design = Design(resume_id=resume_id)
        db.add(design)

    return {
        "success": True,
        "resume_id": str(resume_id),
    }


# //////////////////////////////////////////////////////
# ///////////////////// JOB MATCH //////////////////////
# //////////////////////////////////////////////////////
@resume_router.post("/job-match")
async def job_match(
    payload: ResumeJobMatch,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    user_uuid = UUID(user_id)

    resume_id: str = payload.resume_id
    vacancy_text: str = payload.vacancy_text

    result = await db.execute(
        select(Resume)
        .options(
            selectinload(Resume.experience),
            selectinload(Resume.education),
            selectinload(Resume.languages),
            selectinload(Resume.skills).selectinload(Skills.skills),
        )
        .where(Resume.id == resume_id, Resume.user_id == user_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resume not found"
        )

    raw_resume = {
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
                "language": language.language or "",
                "degree": language.degree or "",
            }
            for language in resume.languages
        ],
        "skills": [
            {
                "title": skills_group.title or "",
                "skills": [{"skill": item.skill or ""} for item in skills_group.skills],
            }
            for skills_group in resume.skills
        ],
    }

    resume_text = json.dumps(raw_resume, ensure_ascii=False)

    input_hash = build_input_hash(resume, vacancy_text)

    hash_resume = await db.execute(
        select(Resume).where(
            Resume.input_hash == input_hash, Resume.user_id == user_uuid
        )
    )

    hash_resume_result = hash_resume.scalar_one_or_none()

    if not hash_resume_result is None:
        return {
            "success": True,
            "resume_id": hash_resume_result.id,
        }

    ai_response = await job_match_resume(
        resume_text=resume_text, vacancy_text=vacancy_text
    )

    if not has_content(ai_response.resume.model_dump()):
        raise HTTPException(
            status_code=422,
            detail={
                "code": "EMPTY_RESUME",
                "message": "Bo'sh resume saqlab bo'lmaydi.",
            },
        )

    personal_data = ai_response.resume.model_dump(
        exclude={
            "experience",
            "education",
            "languages",
            "skills",
        }
    )

    result_resume = Resume(
        user_id=user_uuid,
        parent_resume_id=resume_id,
        job_company=ai_response.job_company,
        job_title=ai_response.job_title,
        cover_letter=ai_response.cover_letter,
        input_hash=input_hash,
        **personal_data,
    )

    result_resume.experience = [
        Experience(**item.model_dump()) for item in ai_response.resume.experience
    ]

    result_resume.education = [
        Education(**item.model_dump()) for item in ai_response.resume.education
    ]

    result_resume.languages = [
        Language(**item.model_dump()) for item in ai_response.resume.languages
    ]

    result_resume.skills = [
        Skills(
            title=group.title,
            skills=[SkillItem(skill=item.skill) for item in group.skills],
        )
        for group in ai_response.resume.skills
    ]

    try:
        db.add(result_resume)
        await db.flush()
        result_resume_id = result_resume.id

        design = Design(resume_id=result_resume_id)
        db.add(design)

        await db.commit()
    except Exception:
        await db.rollback()
        raise

    return {
        "success": True,
        "resume_id": str(result_resume_id),
        "cover_letter": ai_response.cover_letter,
    }


@resume_router.get("/{resume_id}/design")
async def get_resume_design(resume_id: str, db: AsyncSession = Depends(get_db)):
    resume_uuid = UUID(resume_id)

    result = await db.execute(
        select(Resume)
        .options(selectinload(Resume.desing))
        .where(Resume.id == resume_uuid)
    )

    resume = result.scalar_one_or_none()

    if not resume:
        raise HTTPException(
            status_code=404, detail="Design malumotlarini yuklashda hatolik yuz berdi"
        )

    design = resume.desing

    return {
        "template": design.template,
        "heading_title_color": design.heading_title_color,
        "entry_title_color": design.entry_title_color,
        "font": design.font,
    }


logger = logging.getLogger(__name__)


class ResumePdfRequest(BaseModel):
    html: str = Field(min_length=1, max_length=15_000_000)



@resume_router.patch("/edit/{resume_id}/design")
async def design_edit(
    resume_id: str,
    desing_info: DesingInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    resume_uuid = UUID(resume_id)

    result = await db.execute(
        select(Resume)
        .options(selectinload(Resume.desing))
        .where(Resume.id == resume_uuid, Resume.user_id == UUID(user_id))
    )

    resume = result.scalar_one_or_none()

    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="resume topilmadi"
        )

    defaults = {
        "template": "classic",
        "font": "Inter",
    }

    desing = resume.desing

    changes = desing_info.model_dump(exclude_unset=True)

    for field, value in changes.items():
        if value is None and field in defaults:
            value = defaults[field]

        setattr(desing, field, value)

    await db.commit()
