from flask.views import MethodView
from flask_smorest import Blueprint as APIBlueprint

from market.schema.product.brand import BrandListSchema, BrandQueryArgSchema

blp = APIBlueprint('商品品牌管理', __name__, url_prefix='/api/v1/product/brands')


@blp.route('/')
class BrandAPI(MethodView):
    """商品品牌管理API"""

    @blp.arguments(BrandQueryArgSchema, location='query')
    @blp.response(200, BrandListSchema)
    def get(self):
        """品牌管理 查看品牌信息"""
        pass
