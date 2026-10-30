import uuid
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.experience import Experience
    from app.models.educations import Education
    from app.models.languages import Language
    from app.models.skills import Skills
    from app.models.design_info import Design


class Resume(Base):

    __tablename__ = "resume"
    __table_args__ = (
        UniqueConstraint(
            "parent_resume_id", "input_hash", name="uq_resume_variant_hash"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    parent_resume_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("resume.id", ondelete="CASCADE"),
        index=True,
        nullable=True,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), index=True
    )
    user: Mapped["User"] = relationship(back_populates="resumes", lazy="raise")

    fullname: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    title: Mapped[Optional[str]] = mapped_column(String(750), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(254), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    website: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    github_link: Mapped[Optional[str]] = mapped_column(String((2048)), nullable=True)
    linkedin_link: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    job_company: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    job_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    input_hash: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

    experience: Mapped[list["Experience"]] = relationship(
        back_populates="resume",
        cascade="all, delete-orphan",
        lazy="raise",
        order_by="Experience.created_at",
    )
    education: Mapped[list["Education"]] = relationship(
        back_populates="resume",
        cascade="all, delete-orphan",
        lazy="raise",
        order_by="Education.created_at",
    )
    languages: Mapped[list["Language"]] = relationship(
        back_populates="resume",
        cascade="all, delete-orphan",
        lazy="raise",
        order_by="Language.created_at",
    )
    skills: Mapped[list["Skills"]] = relationship(
        back_populates="resume",
        cascade="all, delete-orphan",
        lazy="raise",
        order_by="Skills.created_at",
    )
    desing: Mapped["Design"] = relationship(
        back_populates="resume", cascade="all, delete-orphan", lazy="raise"
    )
