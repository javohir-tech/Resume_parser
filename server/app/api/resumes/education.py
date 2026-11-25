from uuid import UUID

from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import  joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import verify

from app.db.session import get_db

from app.models.resume import Resume
from app.models.educations import Education

from app.schemas.resume_schemas import EducationInfo

education_router = APIRouter(prefix="/education", tags=["Resume Education", "Resume"])


@education_router.post("/{resume_id}")
async def create_education(
    resume_id: UUID,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Create an empty education entry in a resume owned by the user and return its ID."""
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Resume).where(Resume.id == resume_id, Resume.user_id == user_uuid)
    )
    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found among your resumes",
        )

    education = Education(resume_id=resume.id)
    db.add(education)
    await db.commit()
    await db.refresh(education)

    return {"education_id": education.id}


@education_router.patch("/{education_id}")
async def edit_education(
    education_id: UUID,
    education_info: EducationInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Update only the supplied education fields after verifying resume ownership."""
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Education)
        .options(joinedload(Education.resume))
        .where(Education.id == education_id)
    )
    education = result.scalar_one_or_none()

    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Education not found"
        )

    if education.resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    changes = education_info.model_dump(exclude_unset=True)
    for field, value in changes.items():
        setattr(education, field, value)

    await db.commit()


@education_router.delete("/{education_id}")
async def delete_education(
    education_id: UUID,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Delete an education entry after verifying resume ownership."""
    user_uuid = UUID(user_id)

    result = await db.execute(
        select(Education)
        .options(joinedload(Education.resume))
        .where(Education.id == education_id)
    )
    education = result.scalar_one_or_none()

    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Education not found"
        )

    if education.resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    await db.delete(education)
    await db.commit()

    return {"message": "Education deleted successfully"}
