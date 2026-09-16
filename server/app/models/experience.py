import uuid
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING, Optional
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.resume import Resume


class Experience(Base):

    __tablename__ = "experience"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("resume.id"), index=True
    )
    resume: Mapped["Resume"] = relationship(back_populates="experience", lazy="raise")
    position: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    company: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    location: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    startDate: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    endDate: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
