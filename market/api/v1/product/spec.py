from flask.views import MethodView

from market.schema.base import RespSchema
from market.schema.product.spec import (
    SpecCreateSchema,
    SpecListSchema,
    SpecQueryArgSchema,
    SpecSchema,
    SpecUpdateSchema,
)
from market.service.product import spec_service
from market.util.blueprint import APIBlueprint

blp = APIBlueprint('商品服务-商品规格管理', __name__, url_prefix='/api/v1/product/specs')


@blp.route('/')
class SpecAPI(MethodView):
    """商品规格管理API"""

    @blp.arguments(SpecQueryArgSchema, location='query')
    @blp.response(SpecListSchema)
    def get(self, args: dict):
        """商品规格管理 查看规格信息"""
        return spec_service.get_list(args)

    @blp.arguments(SpecCreateSchema(many=True))
    @blp.response(RespSchema)
    def post(self, args: list):
        """商品规格管理 创建规格信息"""
        return spec_service.create_many(args)


@blp.route('/<int:spec_id>')
class SpecByIdAPI(MethodView):
    """商品规格详情管理API"""

    @blp.arguments(SpecUpdateSchema)
    @blp.response(SpecSchema)
    def put(self, args: dict, spec_id: int):
        """商品规格管理 修改规格信息"""
        return spec_service.update(spec_id, args)

    @blp.response(RespSchema)
    def delete(self, spec_id: int):
        """商品规格管理 删除规格信息"""
        return spec_service.delete(spec_id)
