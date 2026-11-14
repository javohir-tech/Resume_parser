from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.core.security import verify
from app.models.job_titles import JobTitles
from app.models.user import User

from app.schemas.job_titles import JobTitlesPayload

from fastapi_filter import FilterDepends
from fastapi_filter.contrib.sqlalchemy import Filter

job_title_router = APIRouter(prefix="/job_titles", tags=["job_titles"])


@job_title_router.post("/add")
async def add_job_title(
    payload: JobTitlesPayload,
    user_id: str = Depends(verify),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(User.id == UUID(user_id)))

    user = result.scalar_one_or_none()

    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    try:
        job_title = JobTitles(title=payload.title.strip())
        db.add(job_title)

        await db.flush()
        await db.commit()
    except:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Job title saqlanmadi"
        )

    return {"success": True, "detail": "Bazaga saqlandi"}


class JobTitlesFilter(Filter):
    search: str | None = None

    class Constants(Filter.Constants):
        model = JobTitles
        search_model_fields = ["title"]


@job_title_router.get("/filter")
async def get_job_titles(
    filters: JobTitlesFilter = FilterDepends(JobTitlesFilter),
    user_id: str = Depends(verify),
    db: AsyncSession = Depends(get_db),
):
    query = (
        filters.filter(select(JobTitles))
        .order_by(JobTitles.created_at.desc(), JobTitles.id.desc())
        .limit(10)
    )

    result = await db.execute(query)
    job_titles = result.scalars().all()

    return [{"title": job_title.title} for job_title in job_titles]
