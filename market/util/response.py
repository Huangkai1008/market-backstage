from flask import Flask

__all__ = ['APIFlask']


class APIFlask(Flask):
    """Custom flask class."""

    def make_response(self, rv):
        if rv is None:
            rv = dict()

        return super().make_response(rv)
