from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    dev: bool = False
    debug: bool = False
    web_log_level: str = "INFO"
    jobs_log_level: str = "INFO"
    colorlog: bool = False
    db_url: str
    echo_sql: bool
    db_pool_size: int = 20
    db_max_overflow: int = 30

    class Config:
        case_sensitive = False


settings = Settings()
