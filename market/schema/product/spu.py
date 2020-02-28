from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.product import Spu
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyAutoSchema,
    SQLAlchemyPkSchema,
)


class SpuSchema(SQLAlchemyPkSchema):
    class Meta:
        model = Spu
        exclude = ['delete_time']


class SpuQueryArgSchema(ListQueryArgSchema):
    pass


class SpuListSchema(ListResultSchema):
    items = fields.List(fields.Nested(SpuSchema))


class SpuBaseSchema(SQLAlchemyAutoSchema):
    sub_title = auto_field()
    unit = auto_field()

    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Spu
        fields = ['sub_title', 'unit']


class SpuCreateSchema(SpuBaseSchema):
    name = auto_field()
    cat_id = auto_field()
    brand_id = auto_field()
    store_id = auto_field()

    class Meta(SpuBaseSchema.Meta):
        fields = ['name', 'sub_title', 'unit', 'cat_id', 'brand_id', 'store_id']


class SpuUpdateSchema(SpuBaseSchema):
    published = auto_field()

    class Meta(SpuBaseSchema.Meta):
        fields = ['sub_title', 'unit', 'published']
