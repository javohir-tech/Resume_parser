import uuid
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.experience import Experience
    from app.models.educations import Education
    from app.models.languages import Language
    from app.models.skills import Skills


class Resume(Base):

    __tablename__ = "resume"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), index=True
    )
    user: Mapped["User"] = relationship(back_populates="resumes", lazy="raise")
    fullname: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    title: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    website: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    github_link: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    linkedin_link: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    summary: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    experience: Mapped[list["Experience"]] = relationship(
        back_populates="resume", cascade="all, delete-orphan", lazy="raise"
    )
    education: Mapped[list["Education"]] = relationship(
        back_populates="resume", cascade="all, delete-orphan", lazy="raise"
    )
    languages: Mapped[list["Language"]] = relationship(
        back_populates="resume", cascade="all, delete-orphan", lazy="raise"
    )
    skills: Mapped[list["Skills"]] = relationship(
        back_populates="resume", cascade="all, delete-orphan", lazy="raise"
    )
