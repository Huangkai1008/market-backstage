from sqlalchemy import UniqueConstraint

from market.constant.product import (
    CATEGORY_DEFAULT_LEVEL,
    CATEGORY_DEFAULT_PARENT_ID,
    SpecType,
)
from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['Category', 'CategorySpec']


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


class CategorySpec(PkModel, SoftDeleteMixin):
    """商品分类规格 用于确定商品的规格模板"""

    __tablename__ = 'product_category_spec'

    __table_args__ = (UniqueConstraint('cat_id', 'name', 'delete_time'),)

    cat_id = db.Column(db.Integer, nullable=False, index=True, comment='商品分类ID')
    name = db.Column(db.String(64), nullable=False, comment='分类规格名称')  # 颜色，内存大小 ...
    spec_type = db.Column(
        db.SmallInteger, nullable=False, index=True, comment=SpecType.desc()
    )
    selectable = db.Column(db.Boolean, nullable=False, comment='是否参与筛选')
