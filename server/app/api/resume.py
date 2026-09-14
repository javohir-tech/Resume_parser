from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.session import get_db
from app.core.security import verify

from app.schemas.resume_schemas import PersonalInfo, ExperienceInfo, EducationInfo

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

    resume = Resume(user_id=user.id)

    db.add(resume)
    await db.commit()
    await db.refresh(resume)

    return {"resume_id": resume.id}


@resume_router.patch("/edit/{resume_id}")
async def resume_edit(
    resume_id: str,
    personalInfo: PersonalInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """
    Resumeni edit qilish
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
            detail="Resumenigizlar orasidan topilmadi",
        )

    changes = personalInfo.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(resume, field, value)

    await db.commit()


@resume_router.delete("/delete/{resume_id}")
async def delete_resume(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """
    Resumeni o'chirish
    """
    resume_uuid = UUID(resume_id)
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Resume).where(Resume.id == resume_uuid, Resume.user_id == user_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resumelaringiz orasidan topilmadi",
        )

    db.delete(resume)
    await db.commit()

    return {"message": "Rezyume o'chirildi"}


# /////////////////////////////////////////////////////////////
# Experience
# /////////////////////////////////////////////////////////////


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


@resume_router.patch("/edit_experince/{experience_id}")
async def edit_experince(
    experience_id: str,
    ExperienceInfo: ExperienceInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """
    Experince edit qilish
    """
    experience_uuid = UUID(experience_id)
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Experience)
        .options(selectinload(Experience.resume))
        .where(Experience.id == experience_uuid)
    )

    experience = result.scalar_one_or_none()

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tajriba topilmadi"
        )

    resume = experience.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Sizni tajribangiz emas"
        )

    changes = ExperienceInfo.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(experience, field, value)

    await db.commit()


@resume_router.delete(
    "/delete_experience/{experience_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_experience(
    experience_id: str,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """
    Experince o'chirish
    """
    experience_uuid = UUID(experience_id)
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Experience)
        .options(selectinload(Experience.resume))
        .where(Experience.id == experience_uuid)
    )

    experience = result.scalar_one_or_none()

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="tajriba topilmadi"
        )

    resume = experience.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="sizga o'zgartirish mumkin emas",
        )


# /////////////////////////////////////////////////////////////
# Educations
# /////////////////////////////////////////////////////////////


@resume_router.post("/create_education/{resume_id}")
async def create_education(
    resume_id: UUID,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Rezyumega ta'lim ma'lumotini qo'shish."""
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Resume).where(Resume.id == resume_id, Resume.user_id == user_uuid)
    )
    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resumelaringiz orasidan topilmadi",
        )

    education = Education(resume_id=resume.id)
    db.add(education)
    await db.commit()
    await db.refresh(education)

    return {"education_id": education.id}


@resume_router.patch("/edit_education/{education_id}")
async def edit_education(
    education_id: UUID,
    education_info: EducationInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Ta'lim ma'lumotini qisman yangilash."""
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Education)
        .options(selectinload(Education.resume))
        .where(Education.id == education_id)
    )
    education = result.scalar_one_or_none()

    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ta'lim ma'lumoti topilmadi"
        )

    if education.resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sizga o'zgartirish mumkin emas",
        )

    changes = education_info.model_dump(exclude_unset=True)
    for field, value in changes.items():
        setattr(education, field, value)

    await db.commit()


@resume_router.delete("/delete_education/{education_id}")
async def delete_education(
    education_id: UUID,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Ta'lim ma'lumotini o'chirish."""
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Education)
        .options(selectinload(Education.resume))
        .where(Education.id == education_id)
    )
    education = result.scalar_one_or_none()

    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ta'lim ma'lumoti topilmadi"
        )

    if education.resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sizga o'chirish mumkin emas",
        )

    await db.delete(education)
    await db.commit()

    return {"message": "Ta'lim ma'lumoti o'chirildi"}
