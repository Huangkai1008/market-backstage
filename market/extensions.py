"""Flask extensions"""
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_smorest import Api

from market.hook.minio import MinioHook
from market.hook.redis import RedisHook
from market.hook.sqla import SqlAHook

api = Api()
db = SqlAHook(session_options=dict(autoflush=False))
migrate = Migrate()
ma = Marshmallow()
minio = MinioHook()
redis = RedisHook()
