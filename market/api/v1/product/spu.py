from flask.views import MethodView

from market.schema.product.spu import (
    SpuCreateSchema,
    SpuListSchema,
    SpuQueryArgSchema,
    SpuSchema,
    SpuUpdateSchema,
)
from market.service.product import spu_service
from market.util.blueprint import APIBlueprint

blp = APIBlueprint('商品服务-商品SPU管理', __name__, url_prefix='/api/v1/product/spu')


@blp.route('/')
class SpuAPI(MethodView):
    """商品Spu管理API"""

    @blp.arguments(SpuQueryArgSchema, location='query')
    @blp.response(SpuListSchema)
    def get(self, args: dict):
        """Spu管理 查看Spu信息"""
        return spu_service.get_list(args)

    @blp.arguments(SpuCreateSchema)
    @blp.response(SpuSchema)
    def post(self, args: dict):
        """Spu管理 创建Spu信息"""
        return spu_service.create(args)


@blp.route('/<int:spu_id>')
class SpuByIdAPI(MethodView):
    """商品Spu详情管理API"""

    @blp.arguments(SpuUpdateSchema)
    @blp.response(SpuSchema)
    def put(self, args: dict, spu_id: int):
        """Spu管理 修改Spu信息"""
        return spu_service.update(spu_id, args)
