"""Application-level configuration model."""
from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_name: str = "OptionsLab API"
    app_env: str = "development"
    frontend_origin: str = Field(default="http://localhost:3000")
