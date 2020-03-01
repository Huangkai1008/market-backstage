from sqlalchemy import UniqueConstraint

from market.constant.product import SpecType
from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['Spec', 'SpecValue']


class Spec(PkModel, SoftDeleteMixin):
    """商品规格"""

    __tablename__ = 'product_spec'

    __table_args__ = (UniqueConstraint('cat_id', 'name', 'delete_time'),)

    cat_id = db.Column(db.Integer, nullable=False, index=True, comment='商品分类ID')
    name = db.Column(db.String(64), nullable=False, comment='规格名称')  # 颜色，内存大小 ...
    spec_type = db.Column(
        db.SmallInteger, nullable=False, index=True, comment=SpecType.desc()
    )
    selectable = db.Column(db.Boolean, nullable=False, comment='是否参与筛选')


class SpecValue(PkModel, SoftDeleteMixin):
    """商品规格值"""

    __tablename__ = 'product_spec_value'

    spec_id = db.Column(db.BigInteger, nullable=False, index=True, comment='商品规格ID')
    value = db.Column(db.String(127), nullable=False, comment='规格值')
