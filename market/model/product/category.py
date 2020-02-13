from sqlalchemy import UniqueConstraint

from market.constant.product import CategorySpecType
from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['ProductCategory', 'ProductCategorySpec']


class ProductCategory(PkModel, SoftDeleteMixin):
    """商品分类"""

    __table_args__ = (UniqueConstraint('cat_name', 'delete_time'),)

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(
        db.Integer, nullable=False, index=True, default=0, comment='父分类，0表示一级分类'
    )
    cat_name = db.Column(db.String(64), nullable=False, comment='分类名称')
    cat_level = db.Column(
        db.SmallInteger, nullable=False, index=True, comment='分类等级，0->1级，1->2级'
    )
    cat_keywords = db.Column(db.String(255), comment='分类关键词')
    cat_icon = db.Column(db.String(255), comment='分类图标')
    cat_desc = db.Column(db.String(255), description='分类描述')


class ProductCategorySpec(PkModel, SoftDeleteMixin):
    """商品分类规格 用于确定商品的规格模板"""

    __table_args__ = (UniqueConstraint('cat_name', 'spec_name', 'delete_time'),)

    cat_id = db.Column(db.Integer, nullable=False, index=True, comment='商品分类ID')
    spec_type = db.Column(
        db.SmallInteger, nullable=False, index=True, comment=CategorySpecType.desc
    )
    spec_name = db.Column(
        db.String(64), nullable=False, comment='分类规格名称'
    )  # 颜色，内存大小 ...
    selectable = db.Column(db.Boolean, nullable=False, comment='是否参与筛选')
