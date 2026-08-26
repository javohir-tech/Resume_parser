from fastapi import FastAPI , Request
from app.api.auth import auth_router
from app.bot.bot_instance import dp
from app.bot.handlers import router as bot_router

dp.include_router(bot_router)

app = FastAPI()

app.include_router(auth_router , prefix="/api")

@app.get("/")
async def root():
    return {"message" : f"server ishlayapti"}