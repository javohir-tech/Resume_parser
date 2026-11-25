from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import auth_router
from app.api.users import user_router
from app.api.job_titles import job_title_router
from app.api.skills_category import skills_category_router
from app.api.skills_title import skills_router
from app.api.resume import resume_router
from app.bot.bot_instance import dp
from app.bot.handlers import router as bot_router

from app.api.resumes.experience import experience_router
from app.api.resumes.education import education_router
from app.api.resumes.language import language_router

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

app.include_router(auth_router, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(resume_router, prefix="/api")
app.include_router(job_title_router, prefix="/api")
app.include_router(skills_category_router, prefix="/api")
app.include_router(skills_router, prefix="/api")

app.include_router(experience_router, prefix="/api/resume")
app.include_router(education_router, prefix="/api/resume")
app.include_router(language_router, prefix="/api/resume")


@app.get("/")
async def root():
    return {"message": f"server ishlayapti"}
