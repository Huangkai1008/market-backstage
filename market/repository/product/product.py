from typing import Type

from market.model.product.product import Sku, Spu
from market.repository.base import CRUDRepository

__all__ = ['SpuRepository', 'SkuRepository']


class SpuRepository(CRUDRepository):
    @property
    def model_class(self) -> Type[Spu]:
        return Spu


class SkuRepository(CRUDRepository):
    @property
    def model_class(self) -> Type[Sku]:
        return Sku
