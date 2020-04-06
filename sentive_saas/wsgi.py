import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "sentive_saas.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()