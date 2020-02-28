from flask.views import MethodView

from market.schema.product.sku import (
    SkuCreateSchema,
    SkuDetailSchema,
    SkuListSchema,
    SkuQueryArgSchema,
    SkuSchema,
    SkuUpdateSchema,
)
from market.service.product import sku_service
from market.util.blueprint import APIBlueprint

blp = APIBlueprint('商品服务-商品SKU管理', __name__, url_prefix='/api/v1/product/sku')


@blp.route('/')
class SkuAPI(MethodView):
    """商品Sku管理API"""

    @blp.arguments(SkuQueryArgSchema, location='query')
    @blp.response(SkuListSchema)
    def get(self, args: dict):
        """Sku管理 查看Sku信息"""
        return sku_service.get_list(args)

    @blp.arguments(SkuCreateSchema)
    @blp.response(SkuSchema)
    def post(self, args: dict):
        """Sku管理 创建Sku信息"""
        return sku_service.create(args)


@blp.route('/<int:sku_id>')
class SkuByIdAPI(MethodView):
    """商品Sku详情管理API"""

    @blp.response(SkuDetailSchema)
    def get(self, sku_id: int):
        """Sku管理 查看Sku详细信息"""
        return sku_service.get(sku_id)

    @blp.arguments(SkuUpdateSchema)
    @blp.response(SkuSchema)
    def put(self, args: dict, sku_id: int):
        """Sku管理 修改Sku信息"""
        return sku_service.update(sku_id, args)
