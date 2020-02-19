from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Optional, Tuple, Type

from sqlalchemy import asc, desc

from market.constant import message as msg
from market.exceptions import MarketBadRequest
from market.extensions import db
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

    @property
    def query_params(self) -> Tuple:
        return tuple()

    @property
    def fuzzy_query_params(self) -> Tuple:
        return tuple()

    @property
    def in_query_params(self) -> Tuple:
        return tuple()

    @property
    def range_query_params(self) -> Tuple:
        return tuple()

    def get_base_queryset(self):
        queryset = db.session.query(self.model_class)
        return queryset

    def get_queryset(self, **kwargs):
        conditions = self._get_conditions(**kwargs)
        sort_conditions = self._get_sort_conditions(**kwargs)
        return self.get_base_queryset().filter(*conditions).order_by(*sort_conditions)

    def _get_conditions(self, **kwargs) -> list:
        conditions = list()
        for param, value in kwargs.items():
            if param in self.query_params:
                conditions.append(getattr(self.model_class, param) == value)
            elif param in self.fuzzy_query_params:
                conditions.append(getattr(self.model_class, param).like(f'%{value}%'))
            elif param in self.in_query_params:
                conditions.append(
                    conditions.append(getattr(self.model_class, param).in_(value))
                )
            elif param in self.range_query_params:
                start, end = value
                if start:
                    conditions.append(getattr(self.model_class, param) >= start)
                if end:
                    conditions.append(getattr(self.model_class, param) <= end)
        return conditions

    def _get_sort_conditions(self, **kwargs) -> list:
        sort_conditions = list()
        if kwargs.get('ordering'):
            ordering = kwargs['ordering']
            self._update_ordering(self.model_class, ordering, sort_conditions)
        return sort_conditions

    def get_all(self, **kwargs) -> List[PkModel]:
        query = self.get_queryset(**kwargs)
        return query.all()

    def get_paginate_all(self, **kwargs) -> Tuple[List[PkModel], int]:
        query = self.get_queryset(**kwargs)
        total = query.count() if kwargs.get('need_total_count') else 0
        if kwargs.get('page') and kwargs.get('size'):
            query = self.and_pagination(query, kwargs['page'], kwargs['size'])
        return query.all(), total

    def create(self, properties: Dict[str, Any], commit: bool = True) -> PkModel:
        instance = self.model_class(**properties)
        db.session.add(instance)
        if commit:
            db.session.commit()
        return instance

    def update(
        self, record_id: int, properties: Dict[str, Any], commit: bool = True
    ) -> PkModel:
        instance = self.model_class.query.with_for_update().get(record_id)
        if not instance:
            raise MarketBadRequest(msg.RECORD_NOT_FOUND_ERROR)

        for key, value in properties.items():
            setattr(instance, key, value)
        if commit:
            db.session.commit()
        return instance

    def delete(self, record_id: int, commit: bool = True):
        self.model_class.query.filter_by(id=record_id).delete()
        if commit:
            db.session.commit()

    def get(self, record_id: int) -> Optional[PkModel]:
        return self.model_class.get(record_id)

    def find(self, row_locked: bool = False, **kwargs) -> Optional[PkModel]:
        query = self.model_class.query.filter_by(**kwargs)
        if row_locked:
            query = query.with_for_update()
        return query.first()
