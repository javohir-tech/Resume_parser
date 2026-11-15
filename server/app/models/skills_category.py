import uuid
from sqlalchemy import String, UUID, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.db.base import Base


class SkillsCategory(Base):
    __tablename__ = "skills_category"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.clock_timestamp(), nullable=False
    )
