import uuid
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.core.config import settings


def create_access_token(user_id: uuid.UUID) -> str:
    payload = {"sub": str(user_id), "exp": datetime.now() + timedelta(days=7)}

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
