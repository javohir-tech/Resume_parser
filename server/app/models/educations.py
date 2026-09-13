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
    resume_id : Mapped[uuid.uuid4] = mapped_column(UUID(as_uuid=True) , ForeignKey("resume.id") , index=True)
    resume : Mapped["Resume"] = relationship(back_populates="education" , lazy="raise")
    degree : Mapped[Optional[str]] = mapped_column(String , nullable=True)
    fieldOfStudy : Mapped[Optional[str]] = mapped_column(String ,  nullable=True)
    institution :  Mapped[Optional[str]] = mapped_column(String , nullable=True)
    location : Mapped[Optional[str]] = mapped_column(String ,  nullable=True)
    start_date : Mapped[Optional[str]] = mapped_column(String , nullable=True)
    start_date : Mapped[Optional[str]] = mapped_column(String , nullable=True)