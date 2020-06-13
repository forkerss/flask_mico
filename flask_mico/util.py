from importlib import import_module
from typing import List


def import_class_in_module(mod_path: str):
    try:
        mod = import_module(mod_path)
    except ModuleNotFoundError:
        mod_path, cls = mod_path.rsplit('.', 1)
    mod = import_module(mod_path)
    return getattr(mod, cls)


def register_extensions(app, extensions: List[str]):
    for ext_path in extensions:
        ext = import_class_in_module(ext_path)
        ext.init_app(app)
