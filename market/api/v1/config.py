from flask.views import MethodView

from market.util.blueprint import APIBlueprint

blp = APIBlueprint('系统配置管理', __name__, url_prefix='/api/v1/configs')


@blp.route('/ping')
class PingAPI(MethodView):
    @blp.response()
    def get(self):
        """系统配置管理 健康监测"""
        return dict(
            name='market-backstage',
            using='flask',
            description='market-backstage is a Market backstage management system with '
            '[flask](https://flask.palletsprojects.com/).',
        )
