from uuid import UUID

from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.core.security import verify

from app.db.session import get_db

from app.models.resume import Resume
from app.models.languages import Language

from app.schemas.resume_schemas import LanguageInfo

language_router = APIRouter(prefix="/language", tags=["Resume Language", "Resume"])


@language_router.post("/{resume_id}")
async def crete_language(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Create an empty language entry in a resume owned by the user and return its ID."""
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

    language = Language(resume_id=resume.id)

    db.add(language)
    await db.commit()
    await db.refresh(language)

    return {"language_id": language.id}


@language_router.patch("/{language_id}")
async def edit_language(
    language_id: str,
    languageInfo: LanguageInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Update only the supplied language fields after verifying resume ownership."""
    user_uuid = UUID(user_id)
    language_uuid = UUID(language_id)

    result = await db.execute(
        select(Language)
        .options(joinedload(Language.resume))
        .where(Language.id == language_uuid)
    )

    language = result.scalar_one_or_none()

    if language is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Language not found"
        )

    resume = language.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    changes = languageInfo.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(language, field, value)

    await db.commit()


@language_router.delete("/{language_id}")
async def delete_language(
    language_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Delete a language entry after verifying resume ownership."""
    user_uuid = UUID(user_id)
    language_uuid = UUID(language_id)

    result = await db.execute(
        select(Language)
        .options(joinedload(Language.resume))
        .where(Language.id == language_uuid)
    )

    language = result.scalar_one_or_none()

    if language is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Language not found"
        )

    resume = language.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    await db.delete(language)
    await db.commit()

    return {"success": True, "detail": "Language deleted successfully"}
