from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.category import Category
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyAutoSchema,
    SQLAlchemyPkSchema,
)


class CategorySchema(SQLAlchemyPkSchema):
    class Meta:
        model = Category


class CategoryQueryArgSchema(ListQueryArgSchema):
    pass


class CategoryListSchema(ListResultSchema):
    items = fields.List(fields.Nested(CategorySchema))


class CategoryBaseSchema(SQLAlchemyAutoSchema):
    keywords = auto_field()
    icon = auto_field()
    desc = auto_field()

    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Category
        fields = ['keywords', 'icon', 'desc']


class CategoryCreateSchema(CategoryBaseSchema):
    parent_id = auto_field(required=False, missing=0)
    name = auto_field()

    class Meta(CategoryBaseSchema.Meta):
        fields = ['parent_id', 'name', 'keywords', 'icon', 'desc']


class CategoryUpdateSchema(CategoryBaseSchema):
    ...
