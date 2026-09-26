from pydantic import BaseModel , ConfigDict

class StrictSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid" , 
        strict=True
    )

class ParsedExperience(StrictSchema):
    position : str  | None 
    company: str | None
    location: str | None
    startDate: str | None
    endDate: str | None
    description: str | None

class ParsedEducation(StrictSchema):
    degree: str | None
    fieldOfStudy: str | None
    institution: str | None
    location: str | None
    startDate: str | None
    endDate: str | None

class ParsedLanguage(StrictSchema):
    language: str | None
    degree: str | None

class ParsedSkillItem(StrictSchema):
    skill: str | None

class ParsedSkillGroup(StrictSchema):
    title : str | None 
    skills : list[ParsedSkillItem]

class ParseResume(StrictSchema):
    fullname : str |  None
    title: str | None
    email: str | None
    phone: str | None
    location: str | None
    website: str | None
    github_link: str | None
    linkedin_link: str | None
    summary: str | None

    experience: list[ParsedExperience]
    education: list[ParsedEducation]
    languages: list[ParsedLanguage]
    skills: list[ParsedSkillGroup]

class ParsedResumeResult(StrictSchema):
    resume : ParseResume
    warning : list[str]

class ResumeImportResume(StrictSchema):
    resume : ParseResume