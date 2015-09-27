import os
from diablofarm.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DJANGO_DEBUG', None) == '1' else False

TEMPLATE_DEBUG = True if os.environ.get('DJANGO_DEBUG', None) == '1' else False

# ---------------------------------------------------------------------------
# Following the heroku instructions - https://devcenter.heroku.com/articles/getting-started-with-django

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default': dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# ---------------------------------------------------------------------------

# Customize the admin template - https://docs.djangoproject.com/en/1.7/intro/tutorial02/
TEMPLATES =[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'diablofarm', 'templates')],
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

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

ADMINS = [os.environ.get('ADMINS', 'your_email@example.com'), ]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Not going to use the default key - we expect this to come from heroku side,
# we are going to use a blank since there should be no key in the repo
#     http://stackoverflow.com/questions/21683846/unable-to-access-heroku-config-vars-from-django-settings-py
#     https://devcenter.heroku.com/articles/buildpack-api
SECRET_KEY = os.environ.get('SECRET_KEY')


# ---------------------------------------------------------------------------
# Django Logging https://docs.python.org/3/howto/logging.html
# ---------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # Formatters specify the layout of log records in the final output
    'formatters': {
        'verbose': {
            # We are dropping off the time and changing the format some for production
            # because heroku logging + logentries will look better this way.
            'format': ('process=%(process)d level=%(levelname)s ' +
                       'filename=%(filename)s line=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': LOGGING_HANDLERS,
    'loggers': LOGGING_LOGGERS,
}