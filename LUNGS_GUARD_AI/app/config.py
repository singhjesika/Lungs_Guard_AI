from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_DIR: str = "models"
    DATA_DIR: str = "data"
    LOG_LEVEL: str = "INFO"
    ALERT_OXYGEN_THRESHOLD: float = 94.0
    REPORT_OUTPUT_DIR: str = "reports/pdf_reports"

    class Config:
        env_file = ".env"

settings = Settings()
