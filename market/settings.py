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

    # SQLAlchemy
    SQLALCHEMY_POOL_SIZE = env.int('SQLALCHEMY_POOL_SIZE')
    SQLALCHEMY_POOL_RECYCLE = env.int('SQLALCHEMY_POOL_RECYCLE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Openapi Doc
    API_TITLE = 'Market Backstage'
    API_VERSION = VERSION
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_JSON_PATH = 'api-spec.json'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_REDOC_URL = (
        'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'
    )
    OPENAPI_SWAGGER_UI_PATH = '/swagger-ui'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    # Redis
    REDIS_URL = env.str('REDIS_URL')
    REDIS_SENTINEL_URL = env.list('REDIS_SENTINEL_URL', list())

    # Minio
    MINIO_ENDPOINT = env.str('MINIO_ENDPOINT')
    MINIO_ACCESS_KEY = env.str('MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY = env.str('MINIO_SECRET_KEY')
    MINIO_SECURE = env.bool('MINIO_SECURE')


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_BACKTRACE = True
    SQLALCHEMY_DATABASE_URI = env.str('DEV_DATABASE_URL')
    OPENAPI_URL_PREFIX = '/'


class TestingConfig(Config):
    TESTING = True
    LOG_BACKTRACE = True
    SQLALCHEMY_DATABASE_URI = env.str('TEST_DATABASE_URL')


class ProductionConfig(Config):
    LOG_BACKTRACE = False
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URL')


config = defaultdict(
    lambda: DevelopmentConfig,
    dict(
        development=DevelopmentConfig,
        testing=TestingConfig,
        production=ProductionConfig,
    ),
)
