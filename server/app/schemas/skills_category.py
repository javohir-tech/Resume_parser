from pydantic import BaseModel, Field, field_validator


class SkillsCatgoryPayload(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=255,
        description="skill category",
        examples=['Front end development , ...']
    )

    @field_validator("title")
    @classmethod
    def rejected_blank_title(cls , value : str) -> str :
        if not value.strip():
            raise ValueError("titleni bosh qoldirmang")
        return value
