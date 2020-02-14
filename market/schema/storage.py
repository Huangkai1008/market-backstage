from flask_smorest.fields import Upload
from webargs import fields

from market.schema.base import ArgSchema, BaseSchema


class StorageObjectCreateSchema(ArgSchema):
    file = Upload(
        description='待上传文件', required=True, error_messages={'required': '待上传文件不能为空'}
    )


class StorageObjectSchema(BaseSchema):
    url = fields.Str(description='文件链接地址')
    etag = fields.Str(description='ETag信息')
    last_modified = fields.Str(description='上次修改时间')
    location = fields.Str(description='区域')
    version_id = fields.Str(description='Version ID')
