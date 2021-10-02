from flask import Flask

__all__ = ['APIFlask']

from market.util import json as json_util


class APIFlask(Flask):
    """Custom flask class."""

    json_encoder = json_util.ExtendedEncoder

    def make_response(self, rv):
        if rv is None:
            rv = dict()

        return super().make_response(rv)
