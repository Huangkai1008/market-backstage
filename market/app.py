"""Create flask application."""
import os

from flask import Flask

from market.extensions import api, db, ma, migrate
from market.logging import configure_logger
from market.util.response import APIFlask


def create_app() -> Flask:
    """Create flask application instance with factory pattern.

    See Also: https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/

    """
    app = APIFlask(__name__)
    configure_app(app)
    configure_logger(app)
    register_extensions(app)
    return app


def configure_app(app: Flask):
    """Configure flask application with config file."""
    from market.settings import config

    app.config.from_object(config.get(os.getenv('FLASK_ENV')))
    app.url_map.strict_slashes = False


def register_extensions(app: Flask):
    """Register flask extensions."""
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db=db)
    ma.init_app(app)
