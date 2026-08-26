from fastapi import FastAPI , Request
from app.core.config import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : f"server ishlayapti"}