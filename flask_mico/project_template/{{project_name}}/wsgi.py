import os

from flask_mico.app import create_app

os.environ.setdefault('FLASKMICO_SETTINGS_MODULE', 'conf.production.settings')
application = create_app()
