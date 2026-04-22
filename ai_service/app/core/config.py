from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Trip Planner Service"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/ai"

    class Config:
        case_sensitive = True

settings = Settings()
