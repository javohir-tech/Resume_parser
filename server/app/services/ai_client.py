import asyncio

from fastapi import HTTPException
from openai import (
    AsyncOpenAI,
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    RateLimitError,
)

from app.core.config import settings


def ai_error(status: int, code: str, message: str):
    raise HTTPException(
        status_code=status,
        detail={"code": code, "message": message},
    )


async def generate_json(system_prompt: str, text: str) -> str:
    if settings.AI_PROVIDER not in {"deepseek", "openai", "gemini"}:
        ai_error(
            503,
            "AI_CONFIG_ERROR",
            "AI provayder sozlamasi noto'g'ri.",
        )

    if not settings.AI_API_KEY:
        ai_error(
            503,
            "AI_NOT_CONFIGURED",
            "AI xizmati hali sozlanmagan.",
        )

    try:
        # SDK retry ham shu umumiy vaqt chegarasi ichida.
        async with asyncio.timeout(settings.AI_TIMEOUT_SECONDS):
            async with AsyncOpenAI(
                api_key=settings.AI_API_KEY,
                base_url=settings.AI_BASE_URL,
                timeout=settings.AI_TIMEOUT_SECONDS,
                max_retries=settings.AI_MAX_RETRIES,
            ) as client:
                response = await client.chat.completions.create(
                    model=settings.AI_MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                        },
                        {
                            "role": "user",
                            "content": text,
                        },
                    ],
                    response_format={"type": "json_object"},
                    max_tokens=settings.AI_MAX_OUTPUT_TOKENS,
                )

        if not response.choices:
            ai_error(502, "AI_EMPTY_RESPONSE", "AI javob qaytarmadi.")

        choice = response.choices[0]

        if choice.finish_reason != "stop":
            ai_error(
                502,
                "AI_INCOMPLETE_RESPONSE",
                "AI javobi to'liq yakunlanmadi.",
            )

        content = choice.message.content

        if not content or not content.strip():
            ai_error(502, "AI_EMPTY_RESPONSE", "AI bo'sh javob qaytardi.")

        return content

    except (TimeoutError, APITimeoutError):
        ai_error(504, "AI_TIMEOUT", "AI uchun kutish vaqti tugadi.")
    except AuthenticationError:
        ai_error(
            503,
            "AI_AUTH_ERROR",
            "AI xizmatiga ulanish sozlamasini tekshirish kerak.",
        )
    except RateLimitError:
        ai_error(
            503,
            "AI_RATE_LIMIT",
            "AI xizmati band. Keyinroq urinib ko'ring.",
        )
    except APIConnectionError:
        ai_error(
            503,
            "AI_CONNECTION_ERROR",
            "AI xizmatiga ulanib bo'lmadi.",
        )
    except APIStatusError as exc:

        ai_error(
            502,
            "AI_PROVIDER_ERROR",
            "AI xizmati so'rovni bajara olmadi.",
        )
