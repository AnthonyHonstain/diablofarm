import os
from diablofarm.settings.common import *


# ---------------------------------------------------------------------------
# SECRET CONFIGURATION
# A special file to contain login/secret info not stored in the public repo
from diablofarm.settings.settings_secret import *
# END SECRET CONFIGURATION
# ---------------------------------------------------------------------------

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Show stack trace for warning - http://stackoverflow.com/questions/11557119/django-how-to-get-stack-traces-for-runtime-warnings
import warnings
warnings.filterwarnings(
    'error', r"DateTimeField .* received a naive datetime",
    RuntimeWarning, r'django\.db\.models\.fields')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# WARNINGS:
# ?: (1_8.W001) The standalone TEMPLATE_* settings were deprecated in Django 1.8 and the TEMPLATES dictionary takes precedence. You must put the values of the following settings into your default TEMPLATES dict: TEMPLATE_DEBUG.
# https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/
# http://stackoverflow.com/questions/29652748/updating-django-template-settings-from-1-7-to-1-8
#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*',]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'diablofarm',
        'USER': DEV_DB_USER,
        'PASSWORD': DEV_DB_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

THIRD_PARTY_APPS += (
    'django_extensions',
    'debug_toolbar',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS