"""商品服务相关的常量"""
from enum import IntEnum


class CategorySpecType(IntEnum):
    """商品分类规格类型"""

    SALE = 1  # 销售规格属性
    DISPLAY = 2  # 展示规格属性

    @classmethod
    def desc(cls):
        return '分类规格类型：1--销售规格属性，2--展示规格属性'
