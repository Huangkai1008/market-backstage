"""Base model classes."""
import datetime as dt

from sqlalchemy import text

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
    create_time = db.Column(db.DateTime, default=dt.datetime.now, comment='创建时间')
    update_time = db.Column(
        db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, comment='更新时间'
    )

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}(id={self.id})>'

    def flush(self):
        db.session.add(self)
        db.session.flush()


class SoftDeleteMixin:
    """Soft-Delete mixin class."""

    delete_time = db.Column(
        db.BigInteger, nullable=False, server_default=text('0'), comment='逻辑删除时间戳'
    )
