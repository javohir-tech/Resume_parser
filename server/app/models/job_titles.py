import uuid
from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class JobTitles(Base):

    __tablename__ = "job_titles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    title : Mapped[str] = mapped_column(String(255) , nullable=False)
