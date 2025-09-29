from .exceptions import (
    ApiError,
    InvalidAccess,
    InvalidInput,
    InvalidMethod
)

def raise_exception(
    status: str = None,
    dev_message: str = None
):
    _exceptions = {
        "INVALID_ACCESS": InvalidAccess,
        "INVALID_INPUT": InvalidInput,
        "INVALID_METHOD": InvalidMethod,
        "_": ApiError
    }

    _status = "_" if status is None or status not in _exceptions else status

    raise _exceptions[_status](status, dev_message)