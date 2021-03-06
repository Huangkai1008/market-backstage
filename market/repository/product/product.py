from typing import Type

from market.model.product.product import Sku, SkuDetail, Spu
from market.repository.base import CRUDRepository

__all__ = ['SpuRepository', 'SkuRepository', 'SkuDetailRepository']


class SpuRepository(CRUDRepository):
    @property
    def model(self) -> Type[Spu]:
        return Spu


class SkuRepository(CRUDRepository):
    @property
    def model(self) -> Type[Sku]:
        return Sku


class SkuDetailRepository(CRUDRepository):
    @property
    def model(self) -> Type[SkuDetail]:
        return SkuDetail
