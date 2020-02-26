from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.brand import Brand
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyAutoSchema,
    SQLAlchemyPkSchema,
)


class BrandSchema(SQLAlchemyPkSchema):
    class Meta:
        model = Brand
        exclude = ['delete_time']


class BrandQueryArgSchema(ListQueryArgSchema):
    pass


class BrandListSchema(ListResultSchema):
    items = fields.List(fields.Nested(BrandSchema))


class BrandBaseSchema(SQLAlchemyAutoSchema):
    logo = auto_field()

    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Brand
        fields = ['logo']


class BrandCreateSchema(BrandBaseSchema):
    name = auto_field()

    class Meta(BrandBaseSchema.Meta):
        fields = ['name', 'logo']


class BrandUpdateSchema(BrandBaseSchema):
    ...
