"""Create flask application."""
import os
import traceback

from flask import Flask, jsonify
from loguru import logger
from webargs.flaskparser import FlaskParser

from market.api.v1 import storage as storage_api
from market.api.v1.product import brand as brand_api
from market.constant import message as msg
from market.exceptions import MarketClientException, MarketException
from market.extensions import api, db, ma, migrate, minio
from market.logging import configure_logger
from market.util import openapi as openapi_util
from market.util.response import APIFlask


def create_app() -> Flask:
    """Create flask application instance with factory pattern.

    See Also: https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/

    """
    app = APIFlask(__name__)
    configure_app(app)
    configure_logger(app)
    register_extensions(app)
    register_api_blueprints()
    register_before_handlers(app)
    register_error_handlers(app)
    register_shell_context(app)
    register_commands(app)
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
    minio.init_app(app)


def register_api_blueprints():
    """Register flask api blueprints."""
    api.spec.components.security_scheme(
        'bearerAuth', {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}
    )
    api.spec.options['security'] = [{'bearerAuth': []}]
    api.ma_plugin.Converter._field2parameter = openapi_util.patched_field2parameter
    FlaskParser.DEFAULT_UNKNOWN_BY_LOCATION['json'] = None

    api.register_blueprint(brand_api.blp)
    api.register_blueprint(storage_api.blp)


def register_before_handlers(app: Flask):
    """Register the before request handlers."""


def register_error_handlers(app: Flask):
    """Register the error handlers."""

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify(dict(message=msg.NOT_FOUND_ERROR)), 404

    @app.errorhandler(Exception)
    def market_exception_handler(error):
        logger.warning(traceback.format_exc())
        if isinstance(error, MarketClientException):
            response = jsonify(dict(error))
            response.status_code = error.status_code
        else:
            logger.error(msg.SERVER_LOG_ERROR)
            error = MarketException(msg.SERVER_UI_ERROR)
            response = jsonify(dict(error))
            response.status_code = error.status_code
        return response


def register_shell_context(app: Flask):
    """Register the shell context processors."""

    def shell_context():
        return dict(db=db)

    app.shell_context_processor(shell_context)


def register_commands(app: Flask):
    """Register click commands"""
