from functools import wraps
from typing import Dict

from cerberus import SchemaError, Validator
from flask import g, request

from app.lib.errors import AppError, InvalidParameterError
from app.log import logger

FIELDSCHEMAS = {
    'Test': {
        "test": {
            "type": "string",
            "regex": r"^[0-9a-zA-Z_]{4,30}$",
            "required": True
        },
    }
}


def validator(schema: Dict,
              in_params: bool = False,
              null: bool = False):
    """validator: validate data according to `schema`
    Args:
        schema: schema to validate data
        in_params: when is_params is true, validate `request.args` data
        null: when null is true, `data` is allowed to be empty

    Usage:
        @validator(schema=ALLSCHEMA["User"], is_params=True, null=True)
        def get(self): 
            ...
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _validator = Validator(schema)
            if in_params:
                doc_data = dict(request.args)
            else:
                # This is the translated `g.data` from the `filters.Translate`
                doc_data = g.get("data", None)
            logger.debug("FieldValidator - data: %s", repr(doc_data))
            # TODO
            if null is False and not doc_data:
                raise InvalidParameterError(
                    "Invalid Request %s" % doc_data)
            if null is False and not isinstance(doc_data, dict):
                raise InvalidParameterError(
                    "Invalid doc %s not a dict." % doc_data)
            try:
                if not _validator.validate(doc_data):
                    raise InvalidParameterError(_validator.errors)
            except SchemaError:
                raise AppError(description="FieldValidator Schema Error")
            return func(*args, **kwargs)
        return wrapper
    return decorate
