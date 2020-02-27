from typing import Type

from market.model.product.store import Store
from market.repository.base import CRUDRepository

__all__ = ['StoreRepository']


class StoreRepository(CRUDRepository):
    @property
    def model_class(self) -> Type[Store]:
        return Store
