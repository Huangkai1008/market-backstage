from market.constant import message as msg
from market.constant.product import CATEGORY_DEFAULT_LEVEL
from market.repository.product import CategoryRepository, category_repo
from market.service.base import CRUDService

__all__ = ['CategoryService']


class CategoryService(CRUDService):
    @property
    def repo(self) -> CategoryRepository:
        return category_repo

    def get_or_error(self, record_id: int, error_msg: str = msg.CATEGORY_NOT_EXIST):
        return super().get_or_error(record_id, error_msg=error_msg)

    def create(self, args: dict, commit: bool = True):
        parent_id = args['parent_id']
        if parent_id:
            parent_category = self.find_or_error(id=parent_id)
            level = parent_category.level + 1
        else:
            level = CATEGORY_DEFAULT_LEVEL
        args['level'] = level
        return super().create(args)
