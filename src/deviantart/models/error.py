from typing import Literal

from .base import ModelBase


class ErrorModel(ModelBase):
    error: Literal['invalid_request', 'unauthorized', 'unverified_account', 'server_error', 'version_error']
    error_description: str
    error_details: dict | None = None
    error_code: str | None = None
