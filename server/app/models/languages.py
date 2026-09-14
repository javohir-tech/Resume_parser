import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.db.base import Base
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.models.resume import Resume


class Language(Base):

    __tablename__ = "language"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("resume.id"), index=True
    )
    resume: Mapped["Resume"] = relationship(back_populates="languages", lazy="raise")
    language : Mapped[Optional[str]] = mapped_column(String , nullable=True)
    degree : Mapped[Optional[str]] = mapped_column(String , nullable=True)
