import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.models.skills import Skills


class SkillItem(Base):

    __tablename__ = "skill_item"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    skills_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("skills.id"), index=True
    )
    skills: Mapped["Skills"] = relationship(back_populates="skills", lazy="raise")
    skill: Mapped[Optional[str]] = mapped_column(String, nullable=True)
