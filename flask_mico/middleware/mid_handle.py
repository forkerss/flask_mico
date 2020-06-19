from typing import Any, List

from flask import Flask

from flask_mico.util import import_attr_in_module


def _handle(app: Flask, mid_: Any, point_name: str = None):
    """
    Args:
        app: a instance of Flask
        mid_: Any object
        point_name: default=None(apply in root app)
    """
    if hasattr(mid_, 'process_request'):
        if callable(mid_.process_request):
            app.before_request_funcs.setdefault(
                point_name, []).append(mid_.process_request)
    if hasattr(mid_, 'process_response'):
        if callable(mid_.process_response):
            app.after_request_funcs.setdefault(
                point_name, []).append(mid_.process_response)


def register_middlewares(app: Flask, middlewares: List[Any]):
    """register middlewares apply in app
    Args:
        app: a instance of Flask
        middlewares: List of mid in order
    """
    for mid_path in middlewares:
        mid_ = import_attr_in_module(mid_path)
        _handle(app, mid_())
