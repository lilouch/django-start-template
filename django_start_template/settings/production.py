'''Use this for production'''

from .base import *
from decouple import config

DEBUG = False
ALLOWED_HOSTS += ['http://domain.com']
WSGI_APPLICATION = 'django_start_template.wsgi.production.application'
