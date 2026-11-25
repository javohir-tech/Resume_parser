from uuid import UUID

from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.core.security import verify

from app.db.session import get_db

from app.models.skills import Skills
from app.models.skill_item import SkillItem

from app.schemas.resume_schemas import SkillItemInfo

skills_item_router = APIRouter(prefix="/skills_item", tags=["skills item"])


@skills_item_router.post("/{skills_groups_id}")
async def skills_group_add_skill(
    skills_groups_id: str,
    skillItemInfo: SkillItemInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Add a skill item after verifying resume ownership and return the new item ID."""
    user_uuid = UUID(user_id)
    skills_groups_uuid = UUID(skills_groups_id)

    result = await db.execute(
        select(Skills)
        .options(joinedload(Skills.resume))
        .where(Skills.id == skills_groups_uuid)
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

    skillItem = SkillItem(skills_id=skills_group.id, skill=skillItemInfo.skill)

    db.add(skillItem)
    await db.commit()
    await db.refresh(skillItem)

    return {"skill_item_id": skillItem.id}


@skills_item_router.delete("/{skillItem_id}")
async def delete_skill_item(
    skillItem_id: str,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Delete a skill item after verifying ownership of its parent resume."""
    user_uuid = UUID(user_id)
    skillItem_uuid = UUID(skillItem_id)

    result = await db.execute(
        select(SkillItem)
        .options(joinedload(SkillItem.skills).joinedload(Skills.resume))
        .where(SkillItem.id == skillItem_uuid)
    )

    skill_item = result.scalar_one_or_none()

    if skill_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill item not found"
        )

    resume = skill_item.skills.resume

    if resume.user_id != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )

    await db.delete(skill_item)
    await db.commit()

    return {"detail": "Skill item deleted successfully"}
