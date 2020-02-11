import logging
from pathlib import Path

from flask import Flask
from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


def configure_logger(app: Flask):
    """Configure logger with flask application"""
    path = Path(app.config['LOG_PATH'])
    if not path.exists():
        path.mkdir(parents=True)
    log_name = Path(path, 'market_{time}.log')

    logger.add(
        log_name,
        encoding='utf-8',
        level=app.config['LOG_LEVEL'],
        backtrace=app.config['LOG_BACKTRACE'],
        rotation='00:00',
        retention=30,
    )
    app.logger.addHandler(InterceptHandler())
