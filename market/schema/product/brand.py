from webargs import fields

from market.model.product.brand import Brand
from market.schema.base import ListQueryArgSchema, ListResultSchema, SQLAlchemyPkSchema


class BrandSchema(SQLAlchemyPkSchema):
    class Meta:
        model = Brand


class BrandQueryArgSchema(ListQueryArgSchema):
    pass


class BrandListSchema(ListResultSchema):
    items = fields.List(fields.Nested(BrandSchema))
