import hashlib
import json
from app.models.resume import Resume

PROMPT_VERSION = "v1"


def resume_for_hash(resume: Resume) -> dict:
    return {
        "title": resume.title,
        "summary": resume.summary,
        "experience": [
            {
                "position": e.position,
                "company": e.company,
                "description": e.description,
            }
            for e in resume.experience
        ],
        "skills": [
            {"title ": s.title, "skills": [item.skill for item in s.skills]}
            for s in resume.skills
        ],
    }


def build_input_hash(resume: Resume, job_text: str):
    payload = json.dumps(
        resume_for_hash(resume), sort_keys=True, ensure_ascii=False, default=str
    )
    job = "".join(job_text.strip()).lower()
    raw = f"{PROMPT_VERSION}|{payload}|{job}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
