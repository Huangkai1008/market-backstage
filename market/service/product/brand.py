from market.repository.product import BrandRepository, brand_repo
from market.service.base import CRUDService

__all__ = ['BrandService']


class BrandService(CRUDService):
    @property
    def repo(self) -> BrandRepository:
        return brand_repo
