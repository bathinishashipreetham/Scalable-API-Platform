from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Scalable API Platform"
    api_version: str = "v1"
    debug: bool = True

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()

