from abc import ABCMeta, abstractmethod

from market.repository.base import CRUDRepository

__all__ = ['BaseService', 'CRUDService']


class BaseService(metaclass=ABCMeta):
    """Base service class."""


class CRUDService(BaseService, metaclass=ABCMeta):
    @property
    @abstractmethod
    def repo(self) -> CRUDRepository:
        pass

    def get_list(self, args: dict) -> dict:
        items, total = self.repo.get_paginate_all(**args)
        return dict(items=items, total=total)

    def create(self, args: dict, commit: bool = True):
        return self.repo.create(args, commit=commit)

    def update(self, record_id: int, args: dict):
        return self.repo.update(record_id, args)

    def delete(self, record_id: int):
        return self.repo.delete(record_id)
