from fastapi import APIRouter , Depends , status 
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.core.security import verify
from app.models.skills_title import SkillsTitle
from app.schemas.skills_title import SkillsTitleAddPayload

from fastapi_filter import FilterDepends
from fastapi_filter.contrib.sqlalchemy import Filter

skills_title_router = APIRouter(prefix="/skills_title" , tags=["Skills titles"])

@skills_title_router.post("/add")
async def add_skills_item(payload : SkillsTitleAddPayload , user_id :str =  Depends(verify) , db : AsyncSession = Depends(get_db)):
    try :
        skills_item = SkillsTitle(title = payload.title.strip())

        db.add(skills_item)

        await db.flush()
        await db.commit()
    except:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail="Bazada saqlanmadi")

    return {
        "success" : True , 
        "detail"  :"bazaga saqlnadi uka"
    }

class SkillsItemFilter(Filter):
    search  : str | None = None

    class Constants(Filter.Constants):
        model =  SkillsTitle 
        search_model_fields = ["title"]

@skills_title_router.get("/filter")
async def get_filtered_skill_items(
    filters : SkillsItemFilter = FilterDepends(SkillsItemFilter) ,
    user_id : str = Depends(verify) ,
    db: AsyncSession = Depends(get_db)):

    query = filters.filter(select(SkillsTitle)).order_by(SkillsTitle.created_at.desc() , SkillsTitle.id.desc()).limit(10)

    result = await db.execute(query)
    skills_items  = result.scalars().all()

    return [{"title" : item.title } for item in skills_items]