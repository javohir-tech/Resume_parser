from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.session import get_db
from app.core.security import verify

from app.schemas.resume_schemas import (
    PersonalInfo,
    ExperienceInfo,
    EducationInfo,
    LanguageInfo,
    SkillItemInfo,
    SkillsInfo,
)

from app.models.user import User
from app.models.resume import Resume
from app.models.experience import Experience
from app.models.educations import Education
from app.models.languages import Language
from app.models.skills import Skills
from app.models.skill_item import SkillItem

resume_router = APIRouter(prefix="/resume", tags=["resume"])


@resume_router.get("/{resume_id}")
async def get_resume(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id=Depends(verify)
):
    """Return resume data using the frontend field names."""
    user_uuid = UUID(user_id)
    resume_uuid = UUID(resume_id)

    result = await db.execute(
        select(Resume)
        .options(
            selectinload(Resume.experience),
            selectinload(Resume.education),
            selectinload(Resume.languages),
            selectinload(Resume.skills),
            selectinload(Resume.skills).selectinload(Skills.skills),
        )
        .where(Resume.id == resume_uuid)
    )

    resume = result.scalar_one_or_none()

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resume Not Found"
        )

    return {
        "id" : resume.fullname ,
        "fullname": resume.fullname or "",
        "title": resume.title or "",
        "email": resume.email or "",
        "phone": resume.phone or "",
        "location": resume.location or "",
        "website": resume.website or "",
        "github_link": resume.github_link or "",
        "linkedin_link": resume.linkedin_link or "",
        "summary": resume.summary or "",
        "experience": [
            {
                "id": experience.id,
                "position": experience.position or "",
                "company": experience.company or "",
                "location": experience.location or "",
                "startDate": experience.startDate or "",
                "endDate": experience.endDate or "",
                "description": experience.description or "",
            }
            for experience in resume.experience
        ],
        "education": [
            {
                "id": education.id,
                "degree": education.degree or "",
                "fieldOfStudy": education.fieldOfStudy or "",
                "institution": education.institution or "",
                "location": education.location or "",
                "startDate": education.startDate or "",
                "endDate": education.endDate or "",
            }
            for education in resume.education
        ],
        "languages": [
            {
                "id": language.id,
                "language": language.language or "",
                "degree": language.degree or "",
            }
            for language in resume.languages
        ],
        "skills": [
            {
                "id": skills_group.id,
                "title": skills_group.title or "",
                "skills": [
                    {"id": item.id, "skill": item.skill or ""}
                    for item in skills_group.skills
                ],
            }
            for skills_group in resume.skills
        ],
    }


@resume_router.get("/my/resumes")
async def get_my_resumes(
    db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    user_uuid = UUID(user_id)

    result = await db.execute(select(Resume).where(Resume.user_id == user_uuid))

    resumes = result.scalars().all()

    return [
        {
            "id": resume.id,
            "fullname": resume.fullname or "",
            "title": resume.title or "",
        }
        for resume in resumes
    ]


# /////////////////////////////////////////////////////////////
# Personal Info
# /////////////////////////////////////////////////////////////


@resume_router.post("/create")
async def create_resume(
    db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Create an empty resume for the authenticated user and return its ID."""

    result = await db.execute(select(User).where(User.id == user_id))

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    resume = Resume(user_id=user.id)

    db.add(resume)
    await db.commit()
    await db.refresh(resume)

    return {"success": True, "resume_id": resume.id}


@resume_router.patch("/edit/{resume_id}")
async def resume_edit(
    resume_id: str,
    personalInfo: PersonalInfo,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    """Update only the supplied personal information fields in a resume owned by the user."""
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

    changes = personalInfo.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(resume, field, value)

    await db.commit()


@resume_router.delete("/delete/{resume_id}")
async def delete_resume(
    resume_id: str, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    """Delete a resume owned by the authenticated user."""
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

    await db.delete(resume)
    await db.commit()

    return {"success" : True, "message": "Resume deleted successfully"}


# /////////////////////////////////////////////////////////////
# Experience
# /////////////////////////////////////////////////////////////


@resume_router.post("/experience/create/{resume_id}")
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


@resume_router.patch("/experience/edit/{experience_id}")
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


@resume_router.delete(
    "/experience/delete/{experience_id}", status_code=status.HTTP_204_NO_CONTENT
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


# /////////////////////////////////////////////////////////////
# Educations
# /////////////////////////////////////////////////////////////


@resume_router.post("/education/create/{resume_id}")
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


@resume_router.patch("/education/edit/{education_id}")
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


@resume_router.delete("/education/delete/{education_id}")
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


# /////////////////////////////////////////////////////////////
# Languages
# /////////////////////////////////////////////////////////////


@resume_router.post("/language/create/{resume_id}")
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


@resume_router.patch("/language/edit/{language_id}")
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


@resume_router.delete("/language/delete/{language_id}")
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

    return {"detail": "Language deleted successfully"}


# /////////////////////////////////////////////////////////////
# Skills
# /////////////////////////////////////////////////////////////


@resume_router.post("/skills/create/{resume_id}")
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


@resume_router.patch("/skills/edit/{skills_id}")
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


@resume_router.delete("/skills/delete/{skills_id}")
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


@resume_router.post("/skill_item/create/{skills_groups_id}")
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


@resume_router.delete("/skill_item/delete/{skillItem_id}")
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
