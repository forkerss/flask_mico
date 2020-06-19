import enum
from typing import Dict

from flask import Flask, jsonify, make_response

from flask_mico.constant import MEDIA_JSON, http_status_message
from flask_mico.log import logger

try:
    from collections import OrderedDict
except:
    OrderedDict = dict


# common errors
ERR_INVALID_PARAMETER = {
    "status": 400,
    "code": 400,
    "message": "Invalid Parameter"
}
ERR_AUTH_REQUIRED = {
    "status": 401,
    "code": 401,
    "message": "Authentication Required"
}
ERR_NOT_SUPPORTED = {
    "status": 404,
    "code": 404,
    "message": "Not Supported"
}
ERR_UNKNOWN = {
    "status": 500,
    "code": 500,
    "message": "Unknown Error"
}


class AppError(Exception):
    def __init__(self, error: Dict = ERR_UNKNOWN,
                 description: str = None, **kwargs):
        """
        Args:
            error: an instance of 'Dict' or 'Enum'
        """
        self._error = error
        if isinstance(error, enum.Enum):
            self._error = error.value
        self._kv = kwargs
        self._error["description"] = description

    @property
    def status(self) -> int:
        return self._error["status"]

    @property
    def code(self) -> int:
        return self._error["code"]

    @property
    def message(self) -> str:
        return self._error["message"]

    @property
    def description(self) -> str:
        return self._error["description"]

    def handle(self):
        body = OrderedDict()
        body["code"] = self.code
        body["message"] = self.message
        body["success"] = False
        body["data"] = self._kv.get("data", None)
        body_ = jsonify(body)
        resp = make_response(body_, self.status)
        resp.content_type = MEDIA_JSON
        logger.debug("AppError: status: %s body: %s, desc: %s",
                     self.code, body_, self.description)
        return resp


class InvalidParameterError(AppError):
    def __init__(self, description=None):
        super().__init__(ERR_INVALID_PARAMETER)
        self._error["description"] = description


class AuthenticationRequiredError(AppError):
    def __init__(self, description=None):
        super().__init__(ERR_AUTH_REQUIRED)
        self._error["description"] = description


class NotSupportedError(AppError):
    def __init__(self, method=None, url=None):
        super().__init__(ERR_NOT_SUPPORTED)
        if method and url:
            self._error["description"] = "method: %s, url: %s" % (method, url)


class HTTPStatus(Exception):
    def __init__(self, body: str, status: int, headers: Dict):
        self.body = body
        self.status = status
        self.headers = headers

    def handle(self):
        return make_response(self.body, self.status, self.headers)
