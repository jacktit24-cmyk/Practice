"""Application-level configuration model."""
from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "OptionsLab API"
    app_env: str = "development"
