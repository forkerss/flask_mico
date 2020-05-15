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
              in_params: bool = False):
    """validator: validate data according to `schema`
    Args:
        schema: schema to validate data
        in_params: when is_params is true, validate `request.args` data

    Usage:
        @validator(schema=ALLSCHEMA["User"], is_params=True)
        def get(self): 
            ...
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            schema_validator(schema, in_params)
            return func(*args, **kwargs)
        return wrapper
    return decorate


def schema_validator(schema: Dict,
                     in_params: bool = False):
    """validator: validate data according to `schema`
    Args:
        schema: schema to validate data
        in_params: when is_params is true, validate `request.args` data
    """
    _validator = Validator(schema)
    if in_params:
        doc_data = dict(request.args)
    else:
        # This is the translated `g.data` from the `filters.Translate`
        doc_data = g.get("data", {})
    logger.debug("FieldValidator - data: %s", repr(doc_data))
    try:
        if not _validator.validate(doc_data):
            raise InvalidParameterError(_validator.errors)
    except SchemaError:
        raise InvalidParameterError(
            description="FieldValidator Schema Error")