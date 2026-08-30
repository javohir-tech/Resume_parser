import uuid
from datetime import datetime, timezone
from typing import Optional  , TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

if TYPE_CHECKING :
    from app.models.user import User
    


class UserSessions(Base):

    __tablename__ = "user_sessions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), index=True
    )
    ip_address: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    user_agent: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    device_type: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    os_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    os_version: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    browser_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    browser_version: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    device_id: Mapped[str] = mapped_column(String, nullable=False, index=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    last_seen_at :  Mapped[datetime] = mapped_column(
        DateTime(timezone=True) , default=lambda : datetime.now(timezone.utc)
    )

    user : Mapped["User"] = relationship(back_populates="sessions")
