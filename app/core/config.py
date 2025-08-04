import json
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class DefaultSettings(BaseSettings):
    app_name: str = "FastAPI Template"
    debug: bool = False
    health_status: str = "ok"


class APISettings(BaseSettings):
    cors_origins: list[str] = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ["*"]
    cors_allow_headers: list[str] = ["*"]

    @field_validator(
        "cors_origins",
        "cors_allow_methods",
        "cors_allow_headers",
        mode="before",
    )
    @classmethod
    def parse_list(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except Exception:
                return [item.strip() for item in v.split(",") if item]
        return v


class Settings(BaseSettings):
    default: DefaultSettings = DefaultSettings()
    api: APISettings = APISettings()

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        env_prefix="BACKEND__",
        env_nested_delimiter="__",
        extra="ignore",
    )


settings = Settings()
