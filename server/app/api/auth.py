# Standard Library
from datetime import datetime, timezone
from uuid import UUID

# Third-party
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

# LOCAL
from app.models.user import User
from app.models.login_code import LoginCode
from app.db.session import get_db
from app.core.security import (
    create_access_token,
    create_refresh_token,
    verify,
    decode_token,
)
from app.schemas.auth_schemas import RefreshToken

auth_router = APIRouter()


@auth_router.post("/auth/telegram/verify")
async def vefiy_code(code: str, db: AsyncSession = Depends(get_db)):
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

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return {
        "success": True,
        "message": "Login successfuld",
        "data": {
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


@auth_router.get("/me")
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


@auth_router.post("/auth/refresh")
async def refresh_token(
    refresh_token: RefreshToken,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(verify),
):
    user_uuid = UUID(user_id)
    result = await db.execute(select(User).where(User.id == user_uuid))

    user = result.scalar_one_or_none()

    payload = decode_token(refresh_token.refresh_token)


    if str(user.id) != payload['sub']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid token"
        )

    access_token = create_access_token(user.id)

    return {"access_token": access_token}
