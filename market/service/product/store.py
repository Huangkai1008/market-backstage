from market.repository.product import StoreRepository, store_repo
from market.service.base import CRUDService

__all__ = ['StoreService']


class StoreService(CRUDService):
    @property
    def repo(self) -> StoreRepository:
        return store_repo
