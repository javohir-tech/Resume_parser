from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class UserSessionResponse(BaseModel):
    id: UUID
    device_id : str | None
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