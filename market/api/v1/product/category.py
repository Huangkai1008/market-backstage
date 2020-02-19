from flask.views import MethodView

from market.schema.product.category import (
    CategoryCreateSchema,
    CategoryListSchema,
    CategoryQueryArgSchema,
    CategorySchema,
)
from market.service.product import category_service
from market.util.blueprint import APIBlueprint

blp = APIBlueprint('商品服务-商品分类管理', __name__, url_prefix='/api/v1/product/categories')


@blp.route('/')
class CategoryAPI(MethodView):
    """商品分类管理API"""

    @blp.arguments(CategoryQueryArgSchema, location='query')
    @blp.response(CategoryListSchema)
    def get(self, args: dict):
        """分类管理 查看分类信息"""
        return category_service.get_list(args)

    @blp.arguments(CategoryCreateSchema, location='query')
    @blp.response(CategorySchema)
    def post(self, args: dict):
        """分类管理 创建分类信息"""
        return category_service.create(args)
