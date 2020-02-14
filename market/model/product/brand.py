from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['Brand']


class Brand(PkModel, SoftDeleteMixin):
    """商品品牌"""

    __tablename__ = 'product_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, comment='品牌名称')
    logo = db.Column(db.String(255), comment='品牌logo')
