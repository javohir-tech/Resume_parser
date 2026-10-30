from typing import Optional

from pydantic import BaseModel, Field


class DesingInfo(BaseModel):
    template: Optional[str] = Field(
        default=None, description="resume template", examples=["classic"]
    )
    heading_title_color: Optional[str] = Field(
        default=None, description="resume head color"
    )
    entry_title_color: Optional[str] = Field(
        default=None, description="resume title color"
    )
    font: Optional[str] = Field(default=None, description="resume text font")


class PersonalInfo(BaseModel):
    """Resume shaxsiy ma'lumotlarini qisman yangilash uchun schema."""

    fullname: Optional[str] = Field(
        default=None,
        description="To'liq ism",
        examples=["Suvonov Javohir"],
        max_length=150,
    )
    title: Optional[str] = Field(
        default=None,
        description="Kasb yoki lavozim",
        examples=["Backend Developer"],
        max_length=750,
    )
    email: Optional[str] = Field(
        default=None,
        description="Email manzil",
        examples=["example@gmail.com"],
        max_length=254,
    )
    phone: Optional[str] = Field(
        default=None,
        description="Telefon raqami",
        examples=["+998901234567"],
        max_length=32,
    )
    location: Optional[str] = Field(
        default=None,
        description="Yashash joyi",
        examples=["Toshkent, O'zbekiston"],
        max_length=150,
    )
    website: Optional[str] = Field(
        default=None,
        description="Shaxsiy sayt",
        examples=["https://example.com"],
        max_length=2048,
    )
    github_link: Optional[str] = Field(
        default=None,
        description="GitHub profil havolasi",
        examples=["https://github.com/username"],
        max_length=2048,
    )
    linkedin_link: Optional[str] = Field(
        default=None,
        description="LinkedIn profil havolasi",
        examples=["https://www.linkedin.com/in/username"],
        max_length=2048,
    )
    summary: Optional[str] = Field(
        default=None,
        description="O'zingiz haqingizda qisqacha ma'lumot",
        examples=["Python va FastAPI bilan ishlaydigan backend dasturchi."],
    )


class EducationInfo(BaseModel):
    """Ta'lim ma'lumotlarini qisman yangilash uchun schema."""

    degree: Optional[str] = Field(
        default=None,
        description="Ta'lim darajasi",
        examples=["Bakalavr"],
        max_length=150,
    )
    fieldOfStudy: Optional[str] = Field(
        default=None,
        description="Ta'lim yo'nalishi",
        examples=["Dasturiy injiniring"],
        max_length=150,
    )
    institution: Optional[str] = Field(
        default=None, description="Ta'lim muassasasi", examples=["TATU"], max_length=200
    )
    location: Optional[str] = Field(
        default=None,
        description="Ta'lim muassasasi manzili",
        examples=["Toshkent"],
        max_length=150,
    )
    startDate: Optional[str] = Field(
        default=None,
        description="Boshlangan vaqti",
        examples=["sep-2022"],
        max_length=64,
    )
    endDate: Optional[str] = Field(
        default=None, description="Tugagan vaqti", examples=["june-2026"], max_length=64
    )


class ExperienceInfo(BaseModel):
    position: Optional[str] = Field(
        default=None,
        description="ishda lavozim",
        examples=["Front end developer"],
        max_length=150,
    )
    company: Optional[str] = Field(
        default=None, description="ish joyi", examples=["Limsa"], max_length=150
    )
    location: Optional[str] = Field(
        default=None, description="ish manzili", examples=["Tashkent"], max_length=150
    )
    startDate: Optional[str] = Field(
        default=None,
        description="boshlangan vaqti",
        examples=["july-2026"],
        max_length=64,
    )
    endDate: Optional[str] = Field(
        default=None, description="tugagan vaqt", examples=["sep-2026"], max_length=64
    )
    description: Optional[str] = Field(
        default=None, description="is tasnnifi", examples=["..."]
    )


class LanguageInfo(BaseModel):
    language: Optional[str] = Field(
        default=None,
        description="Language",
        examples=["English , Russian"],
        max_length=150,
    )
    degree: Optional[str] = Field(
        default=None, description="daraja", examples=["b2"], max_length=150
    )


class SkillsInfo(BaseModel):
    title: Optional[str] = Field(
        default=None,
        description="skill group title",
        examples=["Front End Developer"],
        max_length=150,
    )


class SkillItemInfo(BaseModel):
    skill: Optional[str] = Field(
        default=None, description="skill item", examples=["JavaScript"], max_length=150
    )


class ResumeJobMatch(BaseModel):
    resume_id: str
    vacancy_text: str
