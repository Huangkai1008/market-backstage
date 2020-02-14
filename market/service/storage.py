from loguru import logger

from market.constant.storage import BUCKET_NAME, PART_SIZE
from market.extensions import minio


class StorageService:
    """对象存储服务"""

    @classmethod
    def put_object(cls, file) -> dict:
        if minio.client.bucket_exists(BUCKET_NAME):
            logger.info(f'存储桶{BUCKET_NAME}已经存在')
        else:
            minio.client.make_bucket(BUCKET_NAME)
            minio.set_read_only_bucket_policy(BUCKET_NAME)

        object_name = minio.get_object_name(file.filename)
        result = minio.client.put_object(
            BUCKET_NAME,
            object_name,
            file,
            -1,
            part_size=PART_SIZE,
            content_type=file.mimetype,
        )
        return dict(
            url=minio.get_url(result.bucket_name, result.object_name),
            etag=result.etag,
            last_modified=result.last_modified,
            location=result.location,
            version_id=result.version_id,
        )
