import json
from flask import Flask
from werkzeug.exceptions import HTTPException

from flask_mico.constant import MEDIA_JSON, http_status_message
from flask_mico.log import logger

from .errors import AppError, HTTPStatus

try:
    from collections import OrderedDict
except:
    OrderedDict = dict


def _handle_bad_request(e):
    """handle bad request
    """
    body = OrderedDict()
    body["code"] = e.code
    body["message"] = getattr(
        e, 'description', http_status_message(e.code))
    body["success"] = False
    body["data"] = None
    resp = e.get_response()
    resp.content_type = MEDIA_JSON
    body = json.dumps(body)
    resp.data = body
    logger.debug("HTTPException: status: %s body: %s",
                 e.code, body)
    return resp


def register_errors(app: Flask):
    """Register errors
    """
    app.register_error_handler(AppError, lambda e: e.handle())
    app.register_error_handler(HTTPStatus, lambda e: e.handle())
    app.register_error_handler(HTTPException, _handle_bad_request)
