"""Base model classes."""
import datetime as dt

from market.extensions import db

__all__ = ['Model', 'PkModel', 'SoftDeleteMixin']


class Model(db.Model):
    """Abstract model class."""

    __abstract__ = True

    def __iter__(self):
        for c in self.__table__.columns:
            yield c.name, getattr(self, c.name)


class PkModel(Model):
    """Abstract model class who has primary key."""

    __abstract__ = True

    id = db.Column(db.BigInteger, primary_key=True)
    create_time = db.Column(db.DateTime, default=dt.datetime.now)
    update_time = db.Column(
        db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now
    )

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}(id={self.id})>'


class SoftDeleteMixin:
    """Soft-Delete mixin class."""

    delete_time = db.Column(db.DateTime, comment='逻辑删除时间')
