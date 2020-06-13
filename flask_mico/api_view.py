from flask import jsonify, request
from flask.views import MethodView

from flask_mico import error
from flask_mico.constant import MEDIA_JSON, http_status_message

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class ApiView(MethodView):
    def on_error(self, status, msg=None, data=None):
        body = OrderedDict()
        body["code"] = status
        body["success"] = False
        body["message"] = msg or http_status_message(status)
        body["data"] = data
        return jsonify(body), status, {"Content-Type": MEDIA_JSON}

    def on_success(self, status=200, msg=None, data=None):
        body = OrderedDict()
        body["code"] = status
        body["success"] = True
        body["message"] = msg or http_status_message(status)
        body["data"] = data
        return jsonify(body), status, {"Content-Type": MEDIA_JSON}

    def get(self, *args, **kwargs):
        raise error.NotSupportedError(method="GET", url=request.path)

    def post(self, *args, **kwargs):
        raise error.NotSupportedError(method="POST", url=request.path)

    def put(self, *args, **kwargs):
        raise error.NotSupportedError(method="PUT", url=request.path)

    def delete(self, *args, **kwargs):
        raise error.NotSupportedError(method="DELETE", url=request.path)
