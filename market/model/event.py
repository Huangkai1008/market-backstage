import datetime as dt

from sqlalchemy import event, inspect
from sqlalchemy.orm import Query

from market.extensions import db
from market.model.base import SoftDeleteMixin
from market.model.product.brand import Brand


@event.listens_for(Query, 'before_compile', retval=True)
def soft_delete_query(query):
    for desc in query.column_descriptions:
        entity = desc['entity']
        if entity is None:
            continue

        inspector = inspect(desc['entity'])
        mapper = getattr(inspector, 'mapper', None)
        if mapper and issubclass(mapper.class_, SoftDeleteMixin):
            query = query.enable_assertions(False).filter(entity.delete_time.is_(None))
            break
    return query


@event.listens_for(Query, 'before_compile_delete', retval=True)
def soft_delete(query, delete_context):
    for desc in query.column_descriptions:
        if issubclass(desc['type'], SoftDeleteMixin):
            entity = desc['entity']
            query = query.filter(entity.delete_time.is_(None))
            query.update(dict(delete_time=dt.datetime.now()))
            return db.session.query(Brand).filter(False)
