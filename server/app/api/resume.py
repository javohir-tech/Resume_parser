from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import verify

from app.models.user import User
from app.models.resume import Resume
from app.models.experience import Experience
from app.models.educations import Education
from app.models.languages import Language
from app.models.skills import Skills
from app.models.skill_item import SkillItem

router = APIRouter(prefix="/resume", tags=["resume"])


@router.post("/create")
async def create_resume():
    """
    resume yaratish
    """

    pass
