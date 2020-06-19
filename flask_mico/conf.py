import importlib
import os

settings = importlib.import_module(
    os.getenv('FLASKMICO_SETTINGS_MODULE', 'conf.development.settings'))
