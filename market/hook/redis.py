from typing import List, Optional

from flask import Flask
from loguru import logger
from redis import ConnectionError, StrictRedis
from redis.sentinel import Sentinel

from market.constant import message as msg
from market.exceptions import MarketConfigException
from market.hook.base import BaseHook


class RedisHook(BaseHook):
    """Redis hook to interact with redis server"""

    def __init__(self, app: Flask = None):
        self.app: Optional[Flask] = app
        self.client = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask, redis_conn_name: str = 'redis_default'):
        self.app = app
        if app.config['REDIS_SENTINEL_URL']:
            sentinels = self._get_sentinels(app.config['REDIS_SENTINEL_URL'])
            sentinel = Sentinel(sentinels, socket_timeout=0.1)
            # TODO Read/Write Splitting
            self.client = sentinel.master_for('doge-master', decode_responses=True)
        else:
            redis_url = app.config['REDIS_URL']
            self.client = StrictRedis.from_url(redis_url, decode_responses=True)
        logger.info(f'Initializing redis hook for conn_name {redis_conn_name}')
        self._detect_connectivity()

    @staticmethod
    def _get_sentinels(redis_sentinel_url: List[str]) -> List[tuple]:
        return [tuple(url.split(':')) for url in redis_sentinel_url]

    def _detect_connectivity(self):
        try:
            self.client.ping()
        except ConnectionError:
            raise MarketConfigException(msg.REDIS_CONNECT_ERROR)
