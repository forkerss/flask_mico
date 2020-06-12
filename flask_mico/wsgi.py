import os

from .main import create_app

os.environ.setdefault('FLASKMICO_SETTINGS_MODULE', 'conf.production.settings')
application = create_app()
