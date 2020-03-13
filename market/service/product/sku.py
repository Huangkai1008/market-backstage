from typing import Tuple

from market.extensions import db
from market.repository.product import SkuRepository, sku_detail_repo, sku_repo
from market.service.base import CRUDService

__all__ = ['SkuService']


class SkuService(CRUDService):
    @property
    def repo(self) -> SkuRepository:
        return sku_repo

    @property
    def detail_fields(self) -> Tuple:
        return ('desc',)

    def get(self, record_id: int):
        sku = super().get_or_error(record_id)
        sku_detail = sku_detail_repo.get(record_id) or dict()
        sku_detail = dict(sku_detail)
        sku_detail.pop('id')
        return dict(sku, **sku_detail)

    def create(self, args: dict, commit: bool = True):
        sku_detail = {field: args.pop(field) for field in self.detail_fields}
        sku = self.repo.flush(args)
        sku_detail['id'] = sku.id
        sku_detail_repo.create(sku_detail, commit=False)
        if commit:
            db.session.commit()
        return sku

    def update(self, record_id: int, args: dict, commit: bool = True):
        sku_detail = {field: args.pop(field) for field in self.detail_fields}
        sku = super().update(record_id, args, commit=False)
        sku_detail_repo.update(record_id, sku_detail, commit=commit)
        if commit:
            db.session.commit()
        return sku
