from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:password@172.21.0.18:5432"
    echo_sql: bool = True
    db_pool_size: int = 20
    db_max_overflow: int = 30

    class Config:
        case_sensitive = False

settings = Settings()
