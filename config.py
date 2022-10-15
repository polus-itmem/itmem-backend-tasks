from typing import Optional
from pydantic import BaseSettings, validator, SecretStr
from pathlib import Path


class Settings(BaseSettings):
    db: SecretStr

    host: str
    port: int
    web_secret: SecretStr

    class Config:
        env_file = Path(__file__).parent.joinpath('.env')
        env_file_encoding = 'utf-8'


config = Settings()
