from importlib import import_module
from typing import List

from click import Command


def import_attr_in_module(mod_path: str):
    try:
        mod = import_module(mod_path)
        return mod
    except ModuleNotFoundError:
        mod_path, attr_name = mod_path.rsplit('.', 1)
        mod = import_module(mod_path)
        return getattr(mod, attr_name)


def register_extensions(app, extensions: List[str]):
    for ext_path in extensions:
        ext = import_attr_in_module(ext_path)
        ext.init_app(app)


def register_commands(app, commands: List[callable]):
    for cmd_path in commands:
        cmd = import_attr_in_module(cmd_path)
        if not isinstance(cmd, Command):
            raise TypeError(
                "Register '%s' must be an instance of 'click.Command'" % cmd)
        app.cli.add_command(cmd)
