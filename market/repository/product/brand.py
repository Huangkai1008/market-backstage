from typing import Type

from market.model.product.brand import Brand
from market.repository.base import CRUDRepository

__all__ = ['BrandRepository']


class BrandRepository(CRUDRepository):
    @property
    def model(self) -> Type[Brand]:
        return Brand
