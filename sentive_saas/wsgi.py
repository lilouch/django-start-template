from configurations.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
import os
import sys
import site

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = BASE_DIR
if path not in sys.path:
    sys.path.append(path)

django_project = BASE_DIR+'/sentive_saas'
sys.path.append(BASE_DIR)
sys.path.append(django_project)

# Calculate path to site-packages directory.
python_home = BASE_DIR+'/env'
python_version = '.'.join(map(str, sys.version_info[:2]))
site_packages = python_home + '/lib/python%s/site-packages' % python_version


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sentive_saas.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')


application = get_wsgi_application()
