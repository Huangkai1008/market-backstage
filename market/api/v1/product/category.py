from flask.views import MethodView

from market.schema.base import RespSchema
from market.schema.product.category import (
    CategoryCreateSchema,
    CategoryListSchema,
    CategoryQueryArgSchema,
    CategorySchema,
    CategorySpecCreateSchema,
    CategorySpecListSchema,
    CategorySpecQueryArgSchema,
    CategorySpecSchema,
    CategorySpecUpdateSchema,
    CategoryUpdateSchema,
)
from market.service.product import category_service, category_spec_service
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


@blp.route('/specs')
class CategorySpecAPI(MethodView):
    """商品分类规格管理API"""

    @blp.arguments(CategorySpecQueryArgSchema, location='query')
    @blp.response(CategorySpecListSchema)
    def get(self, args: dict):
        """分类管理 查看分类规格信息"""
        return category_spec_service.get_list(args)

    @blp.arguments(CategorySpecCreateSchema(many=True))
    @blp.response(RespSchema)
    def post(self, args: list):
        """分类管理 创建分类规格信息"""
        return category_spec_service.create_many(args)


@blp.route('/specs/<int:spec_id>')
class CategorySpecByIdAPI(MethodView):
    """商品分类规格详情管理API"""

    @blp.arguments(CategorySpecUpdateSchema)
    @blp.response(CategorySpecSchema)
    def put(self, args: dict, spec_id: int):
        """分类管理 修改分类规格信息"""
        return category_spec_service.update(spec_id, args)

    @blp.response(RespSchema)
    def delete(self, spec_id: int):
        """分类管理 删除分类规格信息"""
        return category_spec_service.delete(spec_id)
