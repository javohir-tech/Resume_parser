from uuid import UUID

from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from app.core.security import verify

from app.db.session import get_db

from app.models.resume import Resume
from app.models.skills import Skills

from app.schemas.resume_schemas import SkillsInfo

skills_router  = APIRouter(prefix="/skills" , tags=["Skills"])


@skills_router.post("/{resume_id}")
async def create_skill_group(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Create an empty skill group in a resume owned by the user and return its ID."""
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

    skills_group = Skills(resume_id=resume.id)

    db.add(skills_group)
    await db.commit()
    await db.refresh(skills_group)

    return {"skills_id": skills_group.id}


@skills_router.patch("/{skills_id}")
async def edit_skills(
    skills_id: str,
    skillsInfo: SkillsInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Update the title of a skill group after verifying resume ownership."""
    user_uuid = UUID(user_id)
    skills_uuid = UUID(skills_id)

    result = await db.execute(
        select(Skills)
        .options(joinedload(Skills.resume))
        .where(Skills.id == skills_uuid)
    )

    skills_group = result.scalar_one_or_none()

    if skills_group is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill group not found"
        )

    resume = skills_group.resume

    if user_uuid != resume.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    changes = skillsInfo.model_dump(exclude_unset=True)

    for filed, value in changes.items():
        setattr(skills_group, filed, value)

    await db.commit()


@skills_router.delete("/{skills_id}")
async def delete_skills(
    skills_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Delete a skill group and its skill items after verifying resume ownership."""
    user_uuid = UUID(user_id)
    skills_uuid = UUID(skills_id)

    result = await db.execute(
        select(Skills)
        .options(joinedload(Skills.resume))
        .where(Skills.id == skills_uuid)
    )

    skills_group = result.scalar_one_or_none()

    if skills_group is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill group not found"
        )

    resume = skills_group.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    await db.delete(skills_group)
    await db.commit()

    return {"detail": "Skill group deleted successfully"}
