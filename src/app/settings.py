from functools import lru_cache

from pydantic import BaseSettings, conint


class Settings(BaseSettings):
    default_password_length: conint(gt=0, le=200) = 10  # type: ignore
    default_has_numbers: bool = True
    default_has_lowercase_chars: bool = True
    default_has_uppercase_chars: bool = True
    default_has_special_chars: bool = True

    class Config:
        case_sensitive = False
        env_prefix = 'WEBAPP_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
