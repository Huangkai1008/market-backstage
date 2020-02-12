"""Custom exceptions."""
from typing import Optional


class MarketException(Exception):
    status_code = 500

    def __init__(self, message: Optional[str] = None):
        super().__init__(message)
        self.message = message

    def __iter__(self):
        for k in ['message']:
            yield k, getattr(self, k)


class MarketConfigException(MarketException):
    pass


class MarketClientException(MarketException):
    ...


class MarketBadRequest(MarketClientException):
    status_code = 400
