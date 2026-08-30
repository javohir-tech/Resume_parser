from uuid import UUID
from fastapi import APIRouter, Depends, status, Request
from fastapi.exceptions import HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify
from app.db.session import get_db
from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.models.user_sessions import UserSessions
from app.schemas.users_schema import UserSessionResponse
from app.services.device import DEVICE_COOKIE_NAME

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/me")
async def get_me(db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)):
    user_uuid = UUID(user_id)

    result = await db.execute(select(User).where(User.id == user_uuid))

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return {
        "username": user.username,
        "id": user_id,
        "full_name": user.full_name,
        "telegram_id": user.telegram_id,
        "registered_at": user.registered_at,
    }


@user_router.get("/me/sessions")
async def get_sessions(
    request: Request, db: AsyncSession = Depends(get_db), user_id: str = Depends(verify)
):
    user_uuid = UUID(user_id)

    current_device_id = request.cookies.get(DEVICE_COOKIE_NAME)

    result = await db.execute(
        select(UserSessions).where(UserSessions.user_id == user_uuid)
    )

    user_sessions = result.scalars().all()

    sessions: list[UserSessionResponse] = [
        {
            "id": session.id,
            "device_id": session.device_id,
            "os_name": session.os_name,
            "os_version": session.os_version,
            "browser_name": session.browser_name,
            "browser_version": session.browser_version,
            "ip_address": session.ip_address,
            "last_seen_at": session.last_seen_at,
            "created_at": session.created_at,
            "is_current": session.device_id == current_device_id,
        }
        for session in user_sessions
    ]

    return {"sessions": sessions}


@user_router.delete("/sessions/{device_id}")
async def revoke_session(
    device_id: str,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    user_uuid = UUID(user_id)
    result = await db.execute(
        select(UserSessions).where(
            UserSessions.device_id == device_id, UserSessions.user_id == user_uuid
        )
    )

    session = result.scalar_one_or_none()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="session topilmadi"
        )

    await db.execute(
        update(RefreshToken)
        .where(RefreshToken.device_id == device_id, RefreshToken.user_id == user_uuid)
        .values(revoked = True)
    )

    await db.delete(session)
    await db.commit()
    return {
        "success" : True , 
        "message" : "session bekor qilindi"
    }
