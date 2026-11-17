import uuid
from sqlalchemy import String , UUID , DateTime , func
from sqlalchemy.orm import Mapped , mapped_column 
from app.db.base import Base

class SkillsTitle(Base):

    __tablename__ = "skills_title"

    id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True) , primary_key=True , default=uuid.uuid4)
    title : Mapped[str] = mapped_column(String(124) ,nullable=False )
    created_at : Mapped[str] = mapped_column(DateTime , server_default=func.clock_timestamp(), nullable=False)