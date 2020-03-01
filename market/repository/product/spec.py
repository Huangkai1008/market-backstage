from typing import Tuple, Type

from market.model.product.spec import Spec
from market.repository.base import CRUDRepository


class SpecRepository(CRUDRepository):
    @property
    def model_class(self) -> Type[Spec]:
        return Spec

    @property
    def query_params(self) -> Tuple:
        return ('cat_id',)
