from sqlalchemy import UniqueConstraint

from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['Brand']


class Brand(PkModel, SoftDeleteMixin):
    """商品品牌"""

    __tablename__ = 'product_brand'

    __table_args__ = (UniqueConstraint('name', 'delete_time'),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, comment='品牌名称')
    logo = db.Column(db.String(255), comment='品牌logo')

    def __repr__(self) -> str:
        return f'<Brand(id={self.id}, name={self.name})>'
