from sqlalchemy import UniqueConstraint

from market.constant.product import SpecType
from market.extensions import db
from market.model.base import PkModel, SoftDeleteMixin

__all__ = ['Spu', 'Sku', 'SkuDetail', 'SkuSpec']


class Spu(PkModel, SoftDeleteMixin):
    """商品SPU"""

    __tablename__ = 'product_spu'

    name = db.Column(db.String(64), nullable=False, index=True, comment='商品名称')
    sub_title = db.Column(db.String(127), comment='副标题')
    unit = db.Column(db.String(32), nullable=False, comment='单位（件/台...）')
    published = db.Column(db.Boolean, nullable=False, default=True, comment='上架状态')
    cat_id = db.Column(db.Integer, nullable=False, index=True, comment='商品分类ID')
    cat_name = db.Column(db.String(64), nullable=False, comment='商品分类名称')
    brand_id = db.Column(db.Integer, nullable=False, index=True, comment='品牌ID')
    brand_name = db.Column(db.String(64), nullable=False, comment='品牌名称')
    store_id = db.Column(db.Integer, nullable=False, index=True, comment='商铺ID')
    store_name = db.Column(db.String(64), nullable=False, comment='商铺名称')


class Sku(PkModel, SoftDeleteMixin):
    """商品SKU"""

    __tablename__ = 'product_sku'

    __table_args__ = (UniqueConstraint('number', 'delete_time'),)

    number = db.Column(db.String(64), nullable=False, comment='SKU编号')
    price = db.Column(db.DECIMAL(10, 2), nullable=False, comment='价格')
    stock = db.Column(db.Integer, nullable=False, default=0, comment='库存')
    sales = db.Column(db.Integer, nullable=False, default=0, comment='销量')


class SkuDetail(PkModel, SoftDeleteMixin):
    """商品SKU详情"""

    __tablename__ = 'product_sku_detail'

    desc = db.Column(db.Text, nullable=False, comment='商品描述')


class SkuSpec(PkModel, SoftDeleteMixin):
    """商品SKU规格信息

    继承分类规格信息，可在分类规格信息上扩展

    """

    __tablename__ = 'product_sku_spec'

    sku_id = db.Column(db.BigInteger, comment='SKU ID')
    name = db.Column(db.String(64), nullable=False, comment='规格名称')  # 颜色，内存大小 ...
    spec_type = db.Column(
        db.SmallInteger, nullable=False, index=True, comment=SpecType.desc()
    )
    value = db.Column(db.String(127), comment='规格值')  # 红色，16GB ...
