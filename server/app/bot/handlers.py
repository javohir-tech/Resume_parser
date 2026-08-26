import secrets
from random import randint
from datetime import datetime, timedelta
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    ContentType,
)
from sqlalchemy import select, update
from app.db.session import async_session_maker
from app.models.user import User
from app.models.login_code import LoginCode

router = Router()


@router.message(Command("start"))
async def handle_start(message: Message):
    async with async_session_maker() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == message.from_user.id)
        )

    user = result.scalar_one_or_none()

    if user:
        await message.answer("Xush kelibsiz! Kod olish uchun /login yozing.")
        return

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Kontakni ulashish", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await message.answer(
        "Xush kelibsiz! Davom etish uchun kontaktingizni ulashing.",
        reply_markup=keyboard,
    )


@router.message(F.content_type == ContentType.CONTACT)
async def handle_contact(message: Message):
    contact = message.contact

    if contact.user_id != message.from_user.id:
        await message.answer("Iltimos  , faqat o'zingizning kontaktingizni ulashing")
        return

    async with async_session_maker() as session:
        new_user = User(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            full_name=f"{message.from_user.first_name} {message.from_user.last_name or ""}".strip(),
            phone_number=contact.phone_number,
        )

        session.add(new_user)
        await session.commit()

    await message.answer(
        "✅ Ro'yxatdan o'tdingiz! Endi /login orqali kod olishingiz mumkin.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("login"))
async def handle_login(messaage: Message):
    async with async_session_maker() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == messaage.from_user.id)
        )

        user = result.scalar_one_or_none()

        if not user:
            await messaage.answer("Avval profilingizni yuboring — /start ni bosing.")
            return

        await session.execute(
            update(LoginCode)
            .where(LoginCode.user_id == user.id, LoginCode.is_used == False)
            .values(is_used=True)
        )

        code = "".join([str(randint(0, 9)) for _ in range(6)])
        new_login_code = LoginCode(
            user_id=user.id, code=code, expires_at=datetime.now() + timedelta(minutes=1)
        )
        session.add(new_login_code)
        await session.commit()

    await messaage.answer(
        f"🔒 Code:\n<code>{code}</code>\n\n1 daqiqa amal qiladi.", parse_mode="HTML"
    )
