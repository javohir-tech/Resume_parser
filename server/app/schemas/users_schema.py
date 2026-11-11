from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID


class UserSessionResponse(BaseModel):
    id: UUID
    device_id: str | None
    os_name: str | None
    os_version: str | None
    browser_name: str | None
    browser_version: str | None
    ip_address: str | None
    last_seen_at: datetime
    created_at: datetime
    is_current: bool

    class Config:
        from_attributes = True


class UserAccountEdit(BaseModel):
    username: Optional[str] = Field(
        default=None,
        description="username",
        examples=["suvonov_javohir1"],
        max_length=64,
    )
    full_name: Optional[str] = Field(
        default=None,
        description="full name",
        examples=["Suvonov Javohir"],
        max_length=255,
    )
