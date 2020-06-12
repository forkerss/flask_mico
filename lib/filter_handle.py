from typing import List, Any

from flask import Flask


def _handle(app: Flask, filter_: Any, point_name: str = None):
    """
    Args:
        app: a instance of Flask
        filter_: Any object
        point_name: default=None(apply in root app)
    """
    if hasattr(filter_, 'process_request'):
        if callable(filter_.process_request):
            app.before_request_funcs.setdefault(
                point_name, []).append(filter_.process_request)
    if hasattr(filter_, 'process_response'):
        if callable(filter_.process_request):
            app.after_request_funcs.setdefault(
                point_name, []).append(filter_.process_response)


def register_filters(app: Flask, filters: List[Any]):
    """register filters apply in app
    Args:
        app: a instance of Flask
        filters: List of filter in order
    """
    for filter_ in filters:
        _handle(app, filter_)
