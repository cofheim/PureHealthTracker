from pydantic import model_validator

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str

    @model_validator(mode="before")
    def get_database_url(cls, values):
        values["DATABASE_URL"] = (
            f"postgresql+asyncpg://{values.get('DB_USER')}:{values.get('DB_PASS')}@{values.get('DB_HOST')}:{values.get('DB_PORT')}/{values.get('DB_NAME')}"
        )

        return values

    class Config:
        env_file = ".env"


settings = Settings()
