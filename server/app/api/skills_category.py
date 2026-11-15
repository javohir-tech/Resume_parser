from uuid import UUID

from fastapi import status, APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import verify
from app.db.session import get_db
from app.schemas.skills_category import SkillsCatgoryPayload
from app.models.skills_category import SkillsCategory

from fastapi_filter import FilterDepends
from fastapi_filter.contrib.sqlalchemy import Filter

skills_category_router = APIRouter(prefix="/skills_category", tags=["Skills Category"])


@skills_category_router.post("/add")
async def skills_category_add(
    payload: SkillsCatgoryPayload,
    user_id: str = Depends(verify),
    db: AsyncSession = Depends(get_db),
):
    try:
        skills_category = SkillsCategory(title=payload.title)

        db.add(skills_category)

        await db.flush()
        await db.commit()
    except:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="db ga saqlanmadi"
        )

    return {
        "success" : True , 
        "detail" : "db saqlandi"
    }


class FilterCategory(Filter):
    search: str | None = None

    class Constants(Filter.Constants):
        model = SkillsCategory
        search_model_fields = ["title"]


@skills_category_router.get("/filter")
async def get_filtered_catrgories(
    filters: FilterCategory = Depends(FilterCategory),
    user_id: str = Depends(verify),
    db: AsyncSession = Depends(get_db),
):
    query = (
        filters.filter(select(SkillsCategory))
        .order_by(SkillsCategory.created_at.desc(), SkillsCategory.id.desc())
        .limit(10)
    )

    result = await db.execute(query)
    categories = result.scalars().all()

    return categories
