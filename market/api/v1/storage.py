from flask.views import MethodView

from market.schema.storage import StorageObjectCreateSchema, StorageObjectSchema
from market.service import storage_service
from market.util.blueprint import APIBlueprint

blp = APIBlueprint('存储管理', __name__, url_prefix='/api/v1/storage')


@blp.route('/objects')
class StorageObjectAPI(MethodView):
    @blp.arguments(StorageObjectCreateSchema, location='files')
    @blp.response(StorageObjectSchema)
    def post(self, files):
        """存储管理 创建对象"""
        return storage_service.put_object(files['file'])
