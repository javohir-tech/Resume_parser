from uuid import UUID

from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload , joinedload

from app.core.security import verify

from app.db.session import get_db

from app.models.resume import Resume
from app.models.experience import Experience

from app.schemas.resume_schemas import ExperienceInfo

experience_router = APIRouter(prefix="/experience", tags=["experience"])


@experience_router.post("/{resume_id}")
async def create_experience(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Create an empty experience entry in a resume owned by the user and return its ID."""
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

    experience = Experience(resume_id=resume.id)

    db.add(experience)
    await db.commit()
    await db.refresh(experience)

    return {"experience_id": experience.id}


@experience_router.patch("/{experience_id}")
async def edit_experince(
    experience_id: str,
    ExperienceInfo: ExperienceInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Update only the supplied experience fields after verifying resume ownership."""
    experience_uuid = UUID(experience_id)
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Experience)
        .options(joinedload(Experience.resume))
        .where(Experience.id == experience_uuid)
    )

    experience = result.scalar_one_or_none()

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found"
        )

    resume = experience.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    changes = ExperienceInfo.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(experience, field, value)

    await db.commit()


@experience_router.delete(
    "/{experience_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_experience(
    experience_id: str,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Delete an experience entry after verifying resume ownership."""
    experience_uuid = UUID(experience_id)
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Experience)
        .options(joinedload(Experience.resume))
        .where(Experience.id == experience_uuid)
    )

    experience = result.scalar_one_or_none()

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found"
        )

    resume = experience.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    await db.delete(experience)
    await db.commit()

    return {"detail": "Experience deleted successfully"}
