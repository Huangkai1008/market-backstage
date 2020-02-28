from market.constant import message as msg
from market.repository.product import StoreRepository, store_repo
from market.service.base import CRUDService

__all__ = ['StoreService']


class StoreService(CRUDService):
    @property
    def repo(self) -> StoreRepository:
        return store_repo

    def get_or_error(self, record_id: int, error_msg: str = msg.STORE_NOT_EXIST):
        return super().get_or_error(record_id, error_msg=error_msg)
