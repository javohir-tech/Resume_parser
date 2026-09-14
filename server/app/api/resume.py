from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.session import get_db
from app.core.security import verify

from app.schemas.resume_schemas import PersonalInfo, ExperienceInfo

from app.models.user import User
from app.models.resume import Resume
from app.models.experience import Experience
from app.models.educations import Education
from app.models.languages import Language
from app.models.skills import Skills
from app.models.skill_item import SkillItem

resume_router = APIRouter(prefix="/resume", tags=["resume"])


@resume_router.post("/create")
async def create_resume(
    db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """
    resume yaratish
    """

    result = await db.execute(select(User).where(User.id == user_id))

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )

    resume = Resume(user.id)

    db.add(resume)
    await db.commit()
    await db.refresh()

    return {"resume_id": resume.id}


@resume_router.patch("/edit/{resume_id}")
async def resume_edit(
    resume_id: str,
    personalInfo: PersonalInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    user_uuid = UUID(user_id)
    resume_uuid = UUID(resume_id)

    result = await db.execute(
        select(Resume).where(Resume.id == resume_uuid, Resume.user_id == user_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resumenigizlar orasidan topilmadi",
        )

    changes = personalInfo.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(resume, field, value)

    await db.commit()


@resume_router.post("/create_experience/{resume_id}")
async def create_experience(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """
    experince yaratish
    """
    user_uuid = UUID(user_id)
    resume_uuid = UUID(resume_id)

    result = await db.execute(
        select(Resume).where(Resume.id == resume_uuid, Resume.user_id == user_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resumelaringiz orasidan topilmadi",
        )

    experience = Experience(resume_id=resume.id)

    db.add(experience)
    await db.commit()
    await db.refresh(experience)

    return {"experience_id": experience.id}


@resume_router.post("/edit_experince/{experience_id}")
async def edit_experince(
    experience_id: str,
    ExperienceInfo: ExperienceInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    experience_uuid = UUID(experience_id)
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Experience).where(Experience.id == experience_uuid)
    )
