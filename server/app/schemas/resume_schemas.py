from typing import Optional

from pydantic import BaseModel, Field


class PersonalInfo(BaseModel):
    """Resume shaxsiy ma'lumotlarini qisman yangilash uchun schema."""

    fullname: Optional[str] = Field(
        default=None, description="To'liq ism", examples=["Suvonov Javohir"]
    )
    title: Optional[str] = Field(
        default=None, description="Kasb yoki lavozim", examples=["Backend Developer"]
    )
    email: Optional[str] = Field(
        default=None, description="Email manzil", examples=["example@gmail.com"]
    )
    phone: Optional[str] = Field(
        default=None, description="Telefon raqami", examples=["+998901234567"]
    )
    location: Optional[str] = Field(
        default=None, description="Yashash joyi", examples=["Toshkent, O'zbekiston"]
    )
    website: Optional[str] = Field(
        default=None, description="Shaxsiy sayt", examples=["https://example.com"]
    )
    github_link: Optional[str] = Field(
        default=None,
        description="GitHub profil havolasi",
        examples=["https://github.com/username"],
    )
    linkedin_link: Optional[str] = Field(
        default=None,
        description="LinkedIn profil havolasi",
        examples=["https://www.linkedin.com/in/username"],
    )
    summary: Optional[str] = Field(
        default=None,
        description="O'zingiz haqingizda qisqacha ma'lumot",
        examples=["Python va FastAPI bilan ishlaydigan backend dasturchi."],
    )


class EducationInfo(BaseModel):
    """Ta'lim ma'lumotlarini qisman yangilash uchun schema."""

    degree: Optional[str] = Field(
        default=None, description="Ta'lim darajasi", examples=["Bakalavr"]
    )
    fieldOfStudy: Optional[str] = Field(
        default=None, description="Ta'lim yo'nalishi", examples=["Dasturiy injiniring"]
    )
    institution: Optional[str] = Field(
        default=None, description="Ta'lim muassasasi", examples=["TATU"]
    )
    location: Optional[str] = Field(
        default=None, description="Ta'lim muassasasi manzili", examples=["Toshkent"]
    )
    startDate: Optional[str] = Field(
        default=None, description="Boshlangan vaqti", examples=["sep-2022"]
    )
    endDate: Optional[str] = Field(
        default=None, description="Tugagan vaqti", examples=["june-2026"]
    )


class ExperienceInfo(BaseModel):
    position: Optional[str] = Field(
        default=None, description="ishda lavozim", examples=["Front end developer"]
    )
    company: Optional[str] = Field(
        default=None, description="ish joyi", examples=["Limsa"]
    )
    location: Optional[str] = Field(
        default=None, description="ish manzili", examples=["Tashkent"]
    )
    startDate: Optional[str] = Field(
        default=None, description="boshlangan vaqti", examples=["july-2026"]
    )
    endDate: Optional[str] = Field(
        default=None, description="tugagan vaqt", examples=["sep-2026"]
    )
    description: Optional[str] = Field(
        default=None, description="is tasnnifi", examples=["..."]
    )


class LanguageInfo(BaseModel):
    language: Optional[str] = Field(
        default=None, description="Language", examples=["English , Russian"]
    )
    degree: Optional[str] = Field(default=None, description="daraja", examples=["b2"])


class SkillsInfo(BaseModel):
    title: Optional[str] = Field(
        default=None, description="skill group title", examples=["Front End Developer"]
    )


class SkillItemInfo(BaseModel):
    skill: Optional[str] = Field(
        default=None, description="skill item", examples=["JavaScript"]
    )
