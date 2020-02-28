from flask import Flask

__all__ = ['APIFlask']

from market.util.json import ExtendedEncoder


class APIFlask(Flask):
    """Custom flask class."""

    json_encoder = ExtendedEncoder

    def make_response(self, rv):
        if rv is None:
            rv = dict()

        return super().make_response(rv)
