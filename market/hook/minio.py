import datetime as dt
import json
from typing import Optional

from flask import Flask
from minio import Minio

from market.constant import message as msg
from market.exceptions import MarketConfigException

__all__ = ['MinioHook']


class MinioHook:
    """Minio hook to interact with minio server"""

    def __init__(self, app: Flask = None):
        self.app: Optional[Flask] = app
        self.client: Optional[Minio] = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.app = app
        endpoint = app.config.get('MINIO_ENDPOINT')
        access_key = app.config.get('MINIO_ACCESS_KEY')
        secret_key = app.config.get('MINIO_SECRET_KEY')
        if not all([endpoint, access_key, secret_key]):
            raise MarketConfigException(msg.MINIO_CONFIG_ERROR)

        self.client = Minio(
            endpoint,
            access_key,
            secret_key,
            secure=app.config.setdefault('MINIO_SECURE', False),
        )

    @property
    def endpoint(self) -> str:
        return self.app.config['MINIO_ENDPOINT']

    def set_read_only_bucket_policy(self, bucket_name: str):
        """Set anonymous read-only bucket policy."""
        policy = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Principal': {'AWS': '*'},
                    'Action': ['s3:GetBucketLocation', 's3:ListBucket'],
                    'Resource': f'arn:aws:s3:::{bucket_name}',
                },
                {
                    'Effect': 'Allow',
                    'Principal': {'AWS': '*'},
                    'Action': ['s3:GetObject'],
                    'Resource': f'arn:aws:s3:::{bucket_name}/*',
                },
            ],
        }
        return self.client.set_bucket_policy(bucket_name, json.dumps(policy))

    def get_object_name(self, object_name: str) -> str:
        """Return generate object name."""
        return f'{self.get_dir_name()}{self.delimiter}{object_name}'

    @staticmethod
    def get_dir_name() -> str:
        """Get directory name as object name prefix."""
        return f'{dt.date.today().strftime("%Y-%m-%d")}'

    @property
    def delimiter(self) -> str:
        return '/'

    def get_url(self, bucket_name: str, object_name: str) -> str:
        return f'{self.endpoint}/{bucket_name}/{object_name}'
