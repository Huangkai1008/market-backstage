from typing import Type

from market.model.product.category import Category, CategorySpec
from market.repository.base import CRUDRepository

__all__ = ['CategoryRepository', 'CategorySpecRepository']


class CategoryRepository(CRUDRepository):
    @property
    def model_class(self) -> Type[Category]:
        return Category


class CategorySpecRepository(CRUDRepository):
    @property
    def model_class(self) -> Type[CategorySpec]:
        return CategorySpec
