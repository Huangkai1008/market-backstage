from market.repository.product import (
    CategoryRepository,
    CategorySpecRepository,
    category_repo,
    category_spec_repo,
)
from market.service.base import CRUDService

__all__ = ['CategoryService', 'CategorySpecService']


class CategoryService(CRUDService):
    @property
    def repo(self) -> CategoryRepository:
        return category_repo


class CategorySpecService(CRUDService):
    @property
    def repo(self) -> CategorySpecRepository:
        return category_spec_repo
