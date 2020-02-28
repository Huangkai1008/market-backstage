from market.constant import message as msg
from market.repository.product import BrandRepository, brand_repo
from market.service.base import CRUDService

__all__ = ['BrandService']


class BrandService(CRUDService):
    @property
    def repo(self) -> BrandRepository:
        return brand_repo

    def get_or_error(self, record_id: int, error_msg: str = msg.BRAND_NOT_EXIST):
        return super().get_or_error(record_id, error_msg=error_msg)
