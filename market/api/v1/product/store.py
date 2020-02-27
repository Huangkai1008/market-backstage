from flask.views import MethodView

from market.schema.base import RespSchema
from market.schema.product.store import (
    StoreCreateSchema,
    StoreListSchema,
    StoreQueryArgSchema,
    StoreSchema,
    StoreUpdateSchema,
)
from market.service.product import store_service
from market.util.blueprint import APIBlueprint

blp = APIBlueprint('商品服务-商铺管理', __name__, url_prefix='/api/v1/product/stores')


@blp.route('/')
class StoreAPI(MethodView):
    """商铺管理API"""

    @blp.arguments(StoreQueryArgSchema, location='query')
    @blp.response(StoreListSchema)
    def get(self, args: dict):
        """商铺管理 查看商铺信息"""
        return store_service.get_list(args)

    @blp.arguments(StoreCreateSchema)
    @blp.response(StoreSchema)
    def post(self, args: dict):
        """商铺管理 创建商铺信息"""
        return store_service.create(args)


@blp.route('/<int:store_id>')
class StoreByIdAPI(MethodView):
    """商铺详情管理API"""

    @blp.arguments(StoreUpdateSchema)
    @blp.response(StoreSchema)
    def put(self, args: dict, store_id: int):
        """商铺管理 修改商铺信息"""
        return store_service.update(store_id, args)

    @blp.response(RespSchema)
    def delete(self, store_id: int):
        """商铺管理 删除商铺信息"""
        return store_service.delete(store_id)
