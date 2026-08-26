import asyncio
from app.bot.bot_instance import bot, dp
from app.bot.handlers import router as bot_router

dp.include_router(bot_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot polling rejimida ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())