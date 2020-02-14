from flask.views import MethodView
from flask_smorest import Blueprint as APIBlueprint

from market.schema.storage import StorageObjectCreateSchema, StorageObjectSchema
from market.service import storage_service

blp = APIBlueprint('存储管理', __name__, url_prefix='/api/v1/storage')


@blp.route('/objects')
class StorageObjectAPI(MethodView):
    @blp.arguments(StorageObjectCreateSchema, location='files')
    @blp.response(200, StorageObjectSchema)
    def post(self, files):
        """创建对象"""
        file = files['file']
        return storage_service.put_object(file)
