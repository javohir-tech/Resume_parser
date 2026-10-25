import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from typing import Optional, TYPE_CHECKING
from app.models.timestampmixin import TimestampMixin

if TYPE_CHECKING:
    from app.models.resume import Resume
    from app.models.skill_item import SkillItem


class Skills(TimestampMixin, Base):

    __tablename__ = "skills"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("resume.id"), index=True
    )
    resume: Mapped["Resume"] = relationship(back_populates="skills", lazy="raise")
    skills: Mapped[list["SkillItem"]] = relationship(
        back_populates="skills", cascade="all, delete-orphan", lazy="raise" , order_by="SkillItem.created_at"
    )
    title: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
