import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings
from yarl import URL

TEMP_DIR = Path(gettempdir())
BASE_DIR = Path(__file__).resolve(strict=True).parent


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = 'NOTSET'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    FATAL = 'FATAL'


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = '0.0.0.0'
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = 'dev'

    log_level: LogLevel = LogLevel.INFO

    # Variables for the database
    db_host: str = 'localhost'
    db_port: int = 5432
    db_user: str = 'backend'
    db_pass: str = 'backend'
    db_base: str = 'backend'
    db_echo: bool = False

    # Authentication settings
    access_token: str = 'sRagTefMlHeGq4Ml1aw07DpQYBOjI4eb'

    cors_origin: str = '*'

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme='postgres',
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f'/{self.db_base}',
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
