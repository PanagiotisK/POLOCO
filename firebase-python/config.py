from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class BaseConfig(BaseSettings):

    FIREBASE_DB_URL: Optional[str]
    FIREBASE_CREDS_JSON: Optional[str]

    """Loads the dotenv file. Including this is necessary to get
    pydantic to load a .env file."""
    model_config = SettingsConfigDict(env_file="/.env", extra="ignore")