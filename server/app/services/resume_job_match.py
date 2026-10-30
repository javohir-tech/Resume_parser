import json

from fastapi import HTTPException
from pydantic import ValidationError

from app.schemas.resume_parse_schema import ParsedResumeResult
from app.services.ai_client import generate_json

SYSTEM_PROMPT = ""


async def job_match_resume(text: str):
    """ ParseResumeResult ni o'zimizga moslashtirishimiz kerak promt  yozish  kerak  """
    schema = json.dumps(ParsedResumeResult.model_json_schema(), ensure_ascii=False)

    raw_resume = await generate_json(system_prompt=SYSTEM_PROMPT + schema, text=text)

