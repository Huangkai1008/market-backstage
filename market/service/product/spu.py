from typing import Optional

from market.repository.product import SpuRepository, spu_repo
from market.service.base import CRUDService

__all__ = ['SpuService']

from market.service.product.brand import BrandService
from market.service.product.category import CategoryService
from market.service.product.store import StoreService


class SpuService(CRUDService):
    """SPU管理服务

    Attributes:
        category_service: 依赖的商品分类服务
        brand_service: 依赖的品牌服务
        store_service: 依赖的商铺服务

    """

    def __init__(
        self,
        category_service: Optional[CategoryService] = None,
        brand_service: Optional[BrandService] = None,
        store_service: Optional[StoreService] = None,
    ):
        self.category_service = category_service or CategoryService()
        self.brand_service = brand_service or BrandService()
        self.store_service = store_service or StoreService()

    @property
    def repo(self) -> SpuRepository:
        return spu_repo

    def create(self, args: dict, commit: bool = True):
        category = self.category_service.get_or_error(args['cat_id'])
        brand = self.brand_service.get_or_error(args['brand_id'])
        store = self.store_service.get_or_error(args['store_id'])
        args['cat_name'] = category.name
        args['brand_name'] = brand.name
        args['store_name'] = store.name
        return super().create(args, commit=commit)
