from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.spec import Spec
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyAutoSchema,
    SQLAlchemyPkSchema,
)
from market.schema.field import RequiredStr


class SpecSchema(SQLAlchemyPkSchema):
    class Meta:
        model = Spec
        exclude = ['delete_time']


class SpecQueryArgSchema(ListQueryArgSchema):
    cat_id = RequiredStr(description='商品分类ID')


class SpecListSchema(ListResultSchema):
    items = fields.List(fields.Nested(SpecSchema))


class SpecBaseSchema(SQLAlchemyAutoSchema):
    spec_type = auto_field()
    selectable = auto_field()

    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Spec
        fields = ['spec_type', 'selectable']


class SpecCreateSchema(SpecBaseSchema):
    name = auto_field()
    cat_id = auto_field()

    class Meta(SpecBaseSchema.Meta):
        fields = ['name', 'cat_id', 'spec_type', 'selectable']


class SpecUpdateSchema(SpecBaseSchema):
    ...
