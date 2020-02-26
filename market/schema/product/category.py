from marshmallow_sqlalchemy import auto_field
from webargs import fields

from market.model.product.category import Category, CategorySpec
from market.schema.base import (
    ListQueryArgSchema,
    ListResultSchema,
    SQLAlchemyAutoSchema,
    SQLAlchemyPkSchema,
)
from market.schema.field import RequiredStr


class CategorySchema(SQLAlchemyPkSchema):
    class Meta:
        model = Category
        exclude = ['delete_time']


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


class CategorySpecSchema(SQLAlchemyPkSchema):
    class Meta:
        model = CategorySpec
        exclude = ['delete_time']


class CategorySpecQueryArgSchema(ListQueryArgSchema):
    cat_id = RequiredStr(description='商品分类ID')


class CategorySpecListSchema(ListResultSchema):
    items = fields.List(fields.Nested(CategorySpecSchema))


class CategorySpecBaseSchema(SQLAlchemyAutoSchema):
    spec_type = auto_field()
    selectable = auto_field()

    class Meta(SQLAlchemyAutoSchema.Meta):
        model = CategorySpec
        fields = ['spec_type', 'selectable']


class CategorySpecCreateSchema(CategorySpecBaseSchema):
    name = auto_field()
    cat_id = auto_field()

    class Meta(CategorySpecBaseSchema.Meta):
        fields = ['name', 'cat_id', 'spec_type', 'selectable']


class CategorySpecUpdateSchema(CategorySpecBaseSchema):
    ...
