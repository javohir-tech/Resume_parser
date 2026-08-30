# Standard Library
from datetime import datetime, timezone
from uuid import UUID

# Third-party
from fastapi import APIRouter, HTTPException, Depends, status, Request, Response
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from slowapi import Limiter
from slowapi.util import get_remote_address
from user_agents import parse

# LOCAL
from app.models.user import User
from app.models.login_code import LoginCode
from app.db.session import get_db
from app.core.security import (
    create_access_token,
    create_refresh_token,
    verify,
    decode_token,
    token_is_valid,
)
from app.models.user_sessions import UserSessions
from app.schemas.auth_schemas import RefreshTokenScheme
from app.models.refresh_token import RefreshToken
from app.services.device import (
    get_or_create_device,
    create_user_session,
    DEVICE_COOKIE_NAME,
)

auth_router = APIRouter(prefix="/auth", tags=["auth"])
limiter = Limiter(key_func=get_remote_address)


@auth_router.post("/telegram/verify")
@limiter.limit("5/minute")
async def vefiy_code(
    request: Request, response: Response, code: str, db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(LoginCode)
        .options(selectinload(LoginCode.user))
        .filter(LoginCode.code == code, LoginCode.is_used == False)
    )

    login_code = result.scalar_one_or_none()

    if not login_code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid verification code"
        )

    if login_code.expires_at < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Verification code has expired",
        )

    login_code.is_used = True
    await db.commit()

    user = login_code.user
    device_id = get_or_create_device(request, response)
    await create_user_session(request, user.id, db, device_id)

    access_token = create_access_token(user.id)
    refresh_token = await create_refresh_token(user.id, device_id, db)

    return {
        "success": True,
        "message": "Login successfuld",
        "data": {
            "device_id": device_id,
            "tokens": {
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            "user": {
                "full_name": user.full_name,
                "id": str(user.id),
                "telegram_id": user.telegram_id,
                "registered_at": user.registered_at,
                "username": user.username,
            },
        },
    }


@auth_router.post("/refresh")
async def refresh_token(
    refresh_token: RefreshTokenScheme,
    db: AsyncSession = Depends(get_db),
):
    payload = decode_token(refresh_token.refresh_token)

    user_id = payload.get("sub")

    user_uuid = UUID(user_id)
    result = await db.execute(select(User).where(User.id == user_uuid))

    user = result.scalar_one_or_none()

    is_valid = await token_is_valid(db, payload["jti"])

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Token not valid"
        )

    if str(user.id) != payload["sub"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
        )

    access_token = create_access_token(user.id)

    return {"access_token": access_token}


@auth_router.post("/logout")
async def handle_logout(
    request: Request,
    refresh_token: RefreshTokenScheme,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    payload = decode_token(refresh_token.refresh_token)
    device_id = request.cookies.get(DEVICE_COOKIE_NAME)
    token_user_id = payload.get("sub", "")
    token_jti = payload.get("jti", "")
    user_uuid = UUID(user_id)

    if user_id != token_user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="token sizga tegishli emas"
        )

    if payload["type"] != "refresh":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token type"
        )

    await db.execute(
        update(RefreshToken)
        .where(RefreshToken.user_id == user_uuid, RefreshToken.jti == token_jti)
        .values(revoked=True)
    )

    result = await db.execute(
        select(UserSessions)
        .where(UserSessions.device_id == device_id, UserSessions.user_id == user_uuid)
    )

    session = result.scalar_one_or_none()

    if session :
        await db.delete(session)
    await db.commit()

    return {"message": "Logged out"}
