from sqlalchemy import UniqueConstraint

from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['Store']


class Store(PkModel, SoftDeleteMixin):
    """商铺"""

    __tablename__ = 'product_store'

    __table_args__ = (UniqueConstraint('name', 'delete_time'),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, comment='商铺名称')
    logo = db.Column(db.String(255), comment='商铺logo')
    desc = db.Column(db.String(255), comment='商铺简介')
