from flask.views import MethodView

from market.schema.base import RespSchema
from market.schema.product.brand import (
    BrandCreateSchema,
    BrandListSchema,
    BrandQueryArgSchema,
    BrandSchema,
    BrandUpdateSchema,
)
from market.service.product import brand_service
from market.util.blueprint import APIBlueprint

blp = APIBlueprint('商品服务-商品品牌管理', __name__, url_prefix='/api/v1/product/brands')


@blp.route('/')
class BrandAPI(MethodView):
    """商品品牌管理API"""

    @blp.arguments(BrandQueryArgSchema, location='query')
    @blp.response(BrandListSchema)
    def get(self, args: dict):
        """品牌管理 查看品牌信息"""
        return brand_service.get_list(args)

    @blp.arguments(BrandCreateSchema, location='query')
    @blp.response(BrandSchema)
    def post(self, args: dict):
        """品牌管理 创建品牌信息"""
        return brand_service.create(args)


@blp.route('/<int:brand_id>')
class BrandByIdAPI(MethodView):
    """商品品牌详情管理API"""

    @blp.arguments(BrandUpdateSchema)
    @blp.response(BrandSchema)
    def put(self, args: dict, brand_id: int):
        """品牌管理 修改品牌信息"""
        return brand_service.update(brand_id, args)

    @blp.response(RespSchema)
    def delete(self, brand_id: int):
        """品牌管理 删除品牌信息"""
        return brand_service.delete(brand_id)
