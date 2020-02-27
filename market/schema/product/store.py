from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.store import Store
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyAutoSchema,
    SQLAlchemyPkSchema,
)


class StoreSchema(SQLAlchemyPkSchema):
    class Meta:
        model = Store
        exclude = ['delete_time']


class StoreQueryArgSchema(ListQueryArgSchema):
    pass


class StoreListSchema(ListResultSchema):
    items = fields.List(fields.Nested(StoreSchema))


class StoreBaseSchema(SQLAlchemyAutoSchema):
    logo = auto_field()
    desc = auto_field()

    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Store
        fields = ['logo', 'desc']


class StoreCreateSchema(StoreBaseSchema):
    name = auto_field()

    class Meta(StoreBaseSchema.Meta):
        fields = ['name', 'logo', 'desc']


class StoreUpdateSchema(StoreBaseSchema):
    ...
