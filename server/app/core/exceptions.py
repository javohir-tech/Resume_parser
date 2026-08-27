from fastapi import Request , status
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded


async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    response =  JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "success": False,
            "message": "Too many attempts. Please try again later.",
        },
    )

    retry_after = getattr(exc , "retry_after" , 60)
    response.headers["Retry-After"] = str(retry_after)
    return response

def register_exception_handlers(app):
    app.add_exception_handler(RateLimitExceeded , rate_limit_handler)