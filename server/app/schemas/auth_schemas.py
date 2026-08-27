from pydantic import BaseModel

class RefreshTokenScheme(BaseModel):
    refresh_token : str