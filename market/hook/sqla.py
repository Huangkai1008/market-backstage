"""Custom Sqlalchemy Hook"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from market.hook.base import BaseHook

__all__ = ['SqlAHook']


class SqlAHook(SQLAlchemy, BaseHook):
    """SQLAlchemy hook to interact with mysql database"""

    def init_app(self, app: Flask):
        super(SqlAHook, self).init_app(app)

    def apply_pool_defaults(self, app, options) -> dict:
        options = super().apply_pool_defaults(app, options)
        options['pool_pre_ping'] = True
        return options
