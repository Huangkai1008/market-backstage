from abc import ABCMeta, abstractmethod
from typing import List, Type

from sqlalchemy import asc, desc

from market.model.base import Model, PkModel

__all__ = ['BaseRepository', 'CRUDRepository']


class BaseRepository(metaclass=ABCMeta):
    """Base repository class."""

    @staticmethod
    def and_pagination(query, page: int = 1, size: int = 10):
        pos = (page - 1) * size
        return query.limit(size).offset(pos)

    @staticmethod
    def _update_ordering(
        model_class: Type[Model], ordering: List[str], sort_conditions: list
    ):
        for field in ordering:
            is_reverse = False
            if field.startswith('-'):
                field = field[1:]
                is_reverse = True

            if not hasattr(model_class, field):
                continue
            sort_condition = (
                desc(getattr(model_class, field))
                if is_reverse
                else asc(getattr(model_class, field))
            )
            sort_conditions.append(sort_condition)


class CRUDRepository(BaseRepository, metaclass=ABCMeta):
    """CRUD repository class."""

    @property
    @abstractmethod
    def model_class(self) -> Type[PkModel]:
        """CRUD model class."""
