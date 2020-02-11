from flask import Flask

__all__ = ['MarketFlask']


class MarketFlask(Flask):
    """Custom flask class."""

    def make_response(self, rv):
        if rv is None:
            rv = dict()

        return super().make_response(rv)
