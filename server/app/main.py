from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import auth_router
from app.bot.bot_instance import dp
from app.bot.handlers import router as bot_router
from app.core.exceptions import register_exception_handlers

dp.include_router(bot_router)

app = FastAPI()

register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth")


@app.get("/")
async def root():
    return {"message": f"server ishlayapti"}
