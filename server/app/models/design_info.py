import uuid
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.resume import Resume


class Design(Base):

    __tablename__ = "desing_info"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("resume.id"), index=True
    )
    template: Mapped[Optional[str]] = mapped_column(String(100), nullable=True , default="classic")
    heading_title_color: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True
    )
    entry_title_color: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    font: Mapped[Optional[str]] = mapped_column(String, nullable=True , default="Inter")
    resume: Mapped[Resume] = relationship(back_populates="desing", lazy="raise")
