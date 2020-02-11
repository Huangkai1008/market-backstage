from collections import defaultdict
from enum import Enum, unique

from environs import Env

env = Env()
env.read_env(override=True)


class Config:
    @unique
    class ServerEnv(Enum):
        DEV = 'development'
        TEST = 'testing'
        PROD = 'production'

    # Project
    VERSION = env.str('VERSION')

    # Flask
    FLASK_ENV = env.str('FLASK_ENV', default=ServerEnv.DEV.value)
    SECRET_KEY = env.str('SECRET_KEY')

    # Logging
    LOG_PATH = env.path('LOG_PATH')
    LOG_LEVEL = env.str('LOG_LEVEL')


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_BACKTRACE = True


class TestingConfig(Config):
    TESTING = True
    LOG_BACKTRACE = True


class ProductionConfig(Config):
    LOG_BACKTRACE = False


config = defaultdict(
    lambda: DevelopmentConfig,
    dict(
        development=DevelopmentConfig,
        testing=TestingConfig,
        production=ProductionConfig,
    ),
)
