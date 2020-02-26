from flask.views import MethodView

from market.schema.base import RespSchema
from market.schema.product.category import (
    CategoryCreateSchema,
    CategoryListSchema,
    CategoryQueryArgSchema,
    CategorySchema,
    CategoryUpdateSchema,
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

    @blp.arguments(CategoryCreateSchema)
    @blp.response(CategorySchema)
    def post(self, args: dict):
        """分类管理 创建分类信息"""
        return category_service.create(args)


@blp.route('/<int:cat_id>')
class CategoryByIdAPI(MethodView):
    """商品分类详情管理API"""

    @blp.arguments(CategoryUpdateSchema)
    @blp.response(CategorySchema)
    def put(self, args: dict, cat_id: int):
        """分类管理 修改分类信息"""
        return category_service.update(cat_id, args)

    @blp.response(RespSchema)
    def delete(self, cat_id: int):
        """分类管理 删除分类信息"""
        return category_service.delete(cat_id)
