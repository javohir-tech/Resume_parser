from app.models.user import User
from app.models.login_code import LoginCode
from datetime import datetime, timezone
from sqlalchemy import select, update
from fastapi import APIRouter, HTTPException, Depends, status
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import create_access_token

auth_router = APIRouter()


@auth_router.post("/telegram/auth/verify")
async def vefiy_code(code: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(LoginCode).where(LoginCode.code == code, LoginCode.is_used == False)
    )

    login_code = result.scalar_one_or_none()

    if not login_code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Natogri kode"
        )

    if login_code.expires_at < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="kod muddati o'tgan"
        )

    login_code.is_used = True
    await db.commit()

    token = create_access_token(login_code.user_id)
    return {"access_token": token, "token_type": "Bearer"}
