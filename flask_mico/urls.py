from importlib import import_module
from inspect import isclass, isfunction
from types import ModuleType
from urllib.parse import urljoin

from flask_mico import ApiView
from flask_mico.log import logger


def include(mod_path: str):
    return import_module(mod_path)


def handle_app_urls(prefix: str, urls_mod):
    for url in urls_mod.urlpatterns:
        if not (isclass(url[1]) and issubclass(url[1], ApiView)):
            logger.error("'%s' Not an instance of 'ApiView'", str(url[1]))
            break
        path = urljoin(prefix, url[0])
        logger.debug('Route %s', path)
        yield path, url[1]


def register_routes(app, urls_path: str):
    def add_url_rule(path, api_cls):
        app.add_url_rule(path, view_func=api_cls.as_view(api_cls.__name__))

    urls_mod = import_module(urls_path)
    logger.debug('register routes %s', urls_mod.urlpatterns)
    for url_ in urls_mod.urlpatterns:
        if isinstance(url_[1], ModuleType):
            for path, view in handle_app_urls(url_[0], url_[1]):
                add_url_rule(path, view)
        elif isclass(url_[1]) and issubclass(url_[1], ApiView):
            add_url_rule(url_[0], url_[1])
        elif isfunction(url_[1]):
            app.add_url_rule(url_[0], endpoint=url_[
                             1].__name__, view_func=url_[1])
