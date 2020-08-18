import json
from flask import Flask, jsonify, make_response
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
    if hasattr(e, "code"):
        body["code"] = e.code
    else:
        body["code"] = 500
    body["message"] = getattr(
        e, 'description', http_status_message(body["code"]))
    body["success"] = False
    body["data"] = None

    if hasattr(e, "get_response"):
        resp = e.get_response()
        resp.data = json.dumps(body)
    else:
        resp = make_response(jsonify(body), body["code"])
    resp.content_type = MEDIA_JSON
    logger.debug("HTTPException: status: %s body: %s",
                 body["code"], body)
    return resp


def register_errors(app: Flask):
    """Register errors
    """
    app.register_error_handler(AppError, lambda e: e.handle())
    app.register_error_handler(HTTPStatus, lambda e: e.handle())
    app.register_error_handler(HTTPException, _handle_bad_request)
