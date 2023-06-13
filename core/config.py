import os
from pydantic import BaseSettings
from dotenv import load_dotenv

# Load environment variable from .env file
load_dotenv()

class Setting(BaseSettings):
    app_name: str
    stage:str

    class Config:
        env_file = ".env"


class LocalSetting(Setting):
    APP_HOST:str
    APP_PORT:str


class ProductionSetting(Setting):
    APP_HOST:str
    APP_PORT:str


def get_config()-> Setting:
    env_stage_name = os.getenv('stage','local')
    config_type = {
        'local': LocalSetting()
    }
    return config_type[env_stage_name]

config: Setting = get_config()



