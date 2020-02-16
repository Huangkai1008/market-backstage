from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.brand import Brand
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyBaseSchema,
    SQLAlchemyPkSchema,
)


class BrandSchema(SQLAlchemyPkSchema):
    class Meta:
        model = Brand


class BrandQueryArgSchema(ListQueryArgSchema):
    pass


class BrandListSchema(ListResultSchema):
    items = fields.List(fields.Nested(BrandSchema))


class BrandBaseSchema(SQLAlchemyBaseSchema):
    logo = auto_field()

    class Meta(SQLAlchemyBaseSchema.Meta):
        model = Brand


class BrandCreateSchema(BrandBaseSchema):
    name = auto_field()
