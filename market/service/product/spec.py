from market.extensions import db
from market.repository.product import spec_repo
from market.repository.product.spec import SpecRepository
from market.service.base import CRUDService


class SpecService(CRUDService):
    @property
    def repo(self) -> SpecRepository:
        return spec_repo

    def create_many(self, args: dict):
        for arg in args:
            self.create(arg, commit=False)
        db.session.commit()
