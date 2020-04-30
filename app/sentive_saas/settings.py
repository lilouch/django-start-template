import os
import json
from django.conf import settings
from decouple import config, Csv
from configurations import Configuration, values
import logging.config


class Base(Configuration):
    # all the base settings here...
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

    SECRET_KEY = config('SECRET_KEY', default='')

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'crispy_forms',
        'imagekit',

        'allauth',
        'allauth.account',
        'allauth.socialaccount',

        'core',
        'user',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = "sentive_saas.urls"

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'sentive_saas.wsgi.application'

    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = 'fr-FR'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
    STATIC_ROOT = os.path.join(BASE_DIR, 'root')
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

    CRISPY_TEMPLATE_PACK = 'bootstrap4'

    LOGIN_REDIRECT_URL = 'dashboard'
    LOGIN_URL = 'login'

    CRISPY_TEMPLATE_PACK = 'bootstrap4'

    # Authentification
    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',
        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    AUTH_USER_MODEL = "core.User"

    SITE_ID = 1

    ACCOUNT_EMAIL_VERIFICATION = 'none'
    LOGIN_REDIRECT_URL = '/'

    
    # Logging Configuration
    # Clear prev config
    LOGGING_CONFIG = None

    # Get loglevel from env
    LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'info').upper()

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console',
            },
        },
        'loggers': {
            '': {
                'level': LOGLEVEL,
                'handlers': ['console', ],
            },
        },
    })


class Dev(Base):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    Base.ALLOWED_HOSTS += ['127.0.0.1', '192.168.99.100']
    '''
    DATABASES = {
        'default': {
            'ENGINE': config('SQL_DATABASE_ENGINE', default=''),
            'NAME': config('SQL_DATABASE_NAME_DEV', default=''),
            'USER': config('SQL_DATABASE_USER_DEV', default=''),
            'PASSWORD': config('SQL_DATABASE_PASSWORD_DEV', default=''),
            'HOST': config('SQL_DATABASE_HOST_DEV', default=''),
            'PORT': config('SQL_DATABASE_PORT_DEV', default=''),
        }
    }
    '''

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(Base.BASE_DIR, 'db.sqlite3'),
        }
    }

    STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', default='')
    STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY', default='')

    SESSION_COOKIE_SECURE = False


class Prod(Base):
    """
    The in-production settings.
    """
    DEBUG = False
    Base.ALLOWED_HOSTS += ['92.243.19.37', '192.168.99.100']
    TEMPLATE_DEBUG = DEBUG

    SESSION_COOKIE_SECURE = False
