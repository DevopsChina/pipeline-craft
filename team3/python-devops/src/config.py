import os

from pydantic import BaseSettings

WORK_DIR = os.path.dirname(__file__)


class Settings(BaseSettings):
    port: int = 8082
    flask_env: str = 'dev'

    mysql_uname: str
    mysql_pwd: str
    mysql_host: str
    mysql_db: str

    redis_uname: str
    redis_host: str

    apm_url: str
    apm_token: str

    class Config:
        flask_env = os.environ.get('env', 'dev')
        env_file = os.path.join(WORK_DIR, 'envs', flask_env + '.env')


setting = Settings()
