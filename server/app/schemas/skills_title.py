from pydantic import BaseModel , Field , field_validator

class SkillsTitleAddPayload(BaseModel):
    title : str = Field(min_length=2 , max_length=124 , description="skill category" , examples=["JavaScript , TypeScript..."])

    @field_validator("title")
    @classmethod 
    def rejected_blank_title(cls , value : str) -> str :
        if not value.strip():
            raise ValueError("title bosh bo'lmasligi kerak")
        return value