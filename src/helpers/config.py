"""
===============================================================================
WHAT: App Configuration & Settings
OVERVIEW: Centralized manager for all environment variables using Pydantic.
HOW IT WORKS: Reads the `.env` file, maps variables to the `Settings` class, 
              and automatically validates their existence and data types.
WHY: Prevents silent bugs by crashing immediately if a variable is missing (fail-fast), 
     enables IDE auto-complete, and avoids scattered `os.getenv()` calls.
===============================================================================
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    GROQ_KEY: str

    class Config:
        env_file =".env"

def get_settings():
    return Settings() 
