import os
import yaml
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


# ─────────── модели ───────────
class DefaultSettings(BaseModel):
    app_name: str = "FastAPI Template"
    debug: bool = False
    health_status: str = "ok"


class APISettings(BaseModel):
    cors_origins: list[str] = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ["*"]
    cors_allow_headers: list[str] = ["*"]


# ─────────── YAML-источник ───────────
def yaml_source() -> dict:
    cfg_path = Path(os.getenv("CONFIG_PATH", BASE_DIR / "config.yaml"))
    if cfg_path.exists():
        with cfg_path.open(encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}        


# ─────────── Settings ───────────
class Settings(BaseSettings):
    default: DefaultSettings = DefaultSettings()
    api: APISettings = APISettings()

    # короткий алиас
    @property
    def app_name(self) -> str:
        return self.default.app_name

    model_config = SettingsConfigDict(
        env_file=".env",                # можно убрать, если не нужен .env
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            yaml_source,          # 1) YAML
            init_settings,        # 2) параметры конструктора
            env_settings,         # 3) ENV
            dotenv_settings,      # 4) .env
            file_secret_settings, # 5) Docker/K8s secrets
        )


settings = Settings()
print(settings.model_dump())
