from uuid import UUID, uuid4
from fastapi import Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user_sessions import UserSessions
from user_agents import parse
from datetime import  datetime  , timezone
from app.core.config import settings

DEVICE_COOKIE_NAME = "device_id"


def get_or_create_device(request: Request, response: Response) -> str:
    device_id = request.cookies.get(DEVICE_COOKIE_NAME)

    if not device_id:
        device_id = str(uuid4())
        response.set_cookie(
            key=DEVICE_COOKIE_NAME,
            value=device_id,
            max_age=60 * 60 * 24 * 365,
            httponly=True,
            secure=settings.DEBUG,
            samesite="lax",
        )
    return device_id


async def create_user_session(
    request: Request, user_id: UUID, session: AsyncSession , device_id : str , 
):
    ua_string = request.headers.get("user-agent", "")
    ip = request.client.host

    result = await session.execute(
        select(UserSessions).where(
            UserSessions.user_id == user_id, UserSessions.device_id == device_id
        )
    )

    existing_session = result.scalar_one_or_none()

    if  existing_session :
        existing_session.ip_address = ip 
        existing_session.last_seen_at = datetime.now(timezone.utc)
        existing_session.user_agent = ua_string
        existing_session.is_active = True
        await session.commit()
        return existing_session

    ua = parse(ua_string)
    new_session = UserSessions(
        user_id=user_id,
        ip_address=ip,
        user_agent=ua_string,
        device_type="mobile" if ua.is_mobile else "tablet" if ua.is_tablet else "pc",
        os_name=ua.os.family,
        os_version=ua.os.version_string,
        browser_name=ua.browser.family,
        browser_version=ua.browser.version_string,
        device_id = device_id
    )

    session.add(new_session)
    await session.commit()
    return new_session
