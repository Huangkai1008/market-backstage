from sqlalchemy import UniqueConstraint

from market.constant.product import CATEGORY_DEFAULT_LEVEL, CATEGORY_DEFAULT_PARENT_ID
from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['Category']


class Category(PkModel, SoftDeleteMixin):
    """商品分类"""

    __tablename__ = 'product_category'

    __table_args__ = (UniqueConstraint('name', 'delete_time'),)

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(
        db.Integer,
        nullable=False,
        index=True,
        default=CATEGORY_DEFAULT_PARENT_ID,
        comment='父分类，0表示一级分类',
    )
    name = db.Column(db.String(64), nullable=False, comment='分类名称')
    level = db.Column(
        db.SmallInteger,
        nullable=False,
        index=True,
        default=CATEGORY_DEFAULT_LEVEL,
        comment='分类等级，0->1级，1->2级',
    )
    keywords = db.Column(db.String(255), comment='分类关键词')
    icon = db.Column(db.String(255), comment='分类图标')
    desc = db.Column(db.String(255), comment='分类描述')
