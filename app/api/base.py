from datetime import datetime

from flask import request, jsonify
from flask.views import MethodView

from app.lib import errors, constant
from app.lib.uitls import http_status_message

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class Api(MethodView):

    def on_error(self, status, msg=None, data=None):
        body = OrderedDict()
        body["code"] = status
        body["success"] = False
        body["message"] = msg or http_status_message(status)
        body["data"] = data
        return jsonify(body), status, {"Content-Type": constant.MEDIA_JSON}

    def on_success(self, status=200, msg=None, data=None):
        body = OrderedDict()
        body["code"] = status
        body["success"] = True
        body["message"] = msg or http_status_message(status)
        body["data"] = data
        return jsonify(body), status, {"Content-Type": constant.MEDIA_JSON}

    def get(self, *args, **kwargs):
        raise errors.NotSupportedError(method="GET", url=request.path)

    def post(self, *args, **kwargs):
        raise errors.NotSupportedError(method="POST", url=request.path)

    def put(self, *args, **kwargs):
        raise errors.NotSupportedError(method="PUT", url=request.path)

    def delete(self, *args, **kwargs):
        raise errors.NotSupportedError(method="DELETE", url=request.path)
