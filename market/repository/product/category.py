from typing import Type

from market.model.product.category import Category
from market.repository.base import CRUDRepository


class CategoryRepository(CRUDRepository):
    @property
    def model(self) -> Type[Category]:
        return Category
