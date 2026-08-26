from app.models.user import User
from app.models.login_code import LoginCode
from datetime import datetime, timezone
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from fastapi import APIRouter, HTTPException, Depends, status
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import create_access_token, create_refresh_token, verify

auth_router = APIRouter()


@auth_router.post("/telegram/auth/verify")
async def vefiy_code(code: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(LoginCode)
        .options(selectinload(LoginCode.user))
        .filter(LoginCode.code == code, LoginCode.is_used == False)
    )

    login_code = result.scalar_one_or_none()

    if not login_code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Natogri kod"
        )

    if login_code.expires_at < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="kod muddati o'tgan"
        )

    login_code.is_used = True
    await db.commit()

    user = login_code.user

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return {
        "success": True,
        "message": "successfuly logged",
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
