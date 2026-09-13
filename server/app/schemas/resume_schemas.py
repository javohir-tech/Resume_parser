from typing import Optional

from pydantic import BaseModel, Field


class PersonalInfo(BaseModel):
    """Resume shaxsiy ma'lumotlarini qisman yangilash uchun schema."""

    fullName: Optional[str] = Field(
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
        default=None, description="GitHub profil havolasi",
        examples=["https://github.com/username"],
    )
    linkedin_link: Optional[str] = Field(
        default=None, description="LinkedIn profil havolasi",
        examples=["https://www.linkedin.com/in/username"],
    )
    summary: Optional[str] = Field(
        default=None, description="O'zingiz haqingizda qisqacha ma'lumot",
        examples=["Python va FastAPI bilan ishlaydigan backend dasturchi."],
    )
