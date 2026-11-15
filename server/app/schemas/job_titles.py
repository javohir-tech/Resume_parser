from pydantic import BaseModel, Field, field_validator


class JobTitlesPayload(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=255,
        description="job title",
        examples=["front end , backend developer"],
    )

    @field_validator("title")
    @classmethod
    def rejected_blanck_title(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("title bosh bo'lmmasligi kerak")
        return value
