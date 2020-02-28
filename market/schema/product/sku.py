from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.product import Sku
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyAutoSchema,
    SQLAlchemyPkSchema,
)


class SkuSchema(SQLAlchemyPkSchema):
    class Meta:
        model = Sku
        exclude = ['delete_time']


class SkuDetailSchema(SkuSchema):
    desc = fields.Str(description='商品描述')


class SkuQueryArgSchema(ListQueryArgSchema):
    pass


class SkuListSchema(ListResultSchema):
    items = fields.List(fields.Nested(SkuSchema))


class SkuBaseSchema(SQLAlchemyAutoSchema):
    price = auto_field()
    desc = fields.Str(required=True, description='商品描述')

    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Sku
        fields = ['price', 'desc']


class SkuCreateSchema(SkuBaseSchema):
    number = auto_field()

    class Meta(SkuBaseSchema.Meta):
        fields = ['number', 'price', 'desc']


class SkuUpdateSchema(SkuBaseSchema):
    ...
