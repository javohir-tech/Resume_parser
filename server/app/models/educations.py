import uuid
from typing import Optional , TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

if TYPE_CHECKING :
    from app.models.resume import Resume

class Education(Base):

    __tablename__ = "education"

    id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True) , primary_key=True , default=uuid.uuid4)
    resume_id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True) , ForeignKey("resume.id") , index=True)
    resume : Mapped["Resume"] = relationship(back_populates="education" , lazy="raise")

    degree : Mapped[Optional[str]] = mapped_column(String(150) , nullable=True)
    fieldOfStudy : Mapped[Optional[str]] = mapped_column(String(150) ,  nullable=True)
    institution :  Mapped[Optional[str]] = mapped_column(String(200) , nullable=True)
    location : Mapped[Optional[str]] = mapped_column(String(150) ,  nullable=True)
    startDate : Mapped[Optional[str]] = mapped_column(String(64) , nullable=True)
    endDate : Mapped[Optional[str]] = mapped_column(String(64) , nullable=True)
