"""
Django settings for ephemeral project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$7q7npzym@k@sy@6xc&0)#bff6zlj_-#0^5=)!zbkghb12z)r@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.generic',
    'apps.account',
    'apps.business',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
    'apps.account.middleware.RequireLoginMiddleware',
)

LOGIN_URL = '/login/'

# PUBLIC_URLS = (
#     r'/api/auth'
# )

LOGIN_REQUIRED_URLS = (
    r'^/conta/*.*$',
    r'^/business/*.*$',
)

ROOT_URLCONF = 'urls'


SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_SERIALIZER='django.contrib.sessions.serializers.JSONSerializer'
SESSION_SAVE_EVERY_REQUEST=True

# Template URLs
## http://designscrazed.org/best-html-ecommerce-website-templates/
## http://demo.themeum.com/html/eshopper/
TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]


WSGI_APPLICATION = 'settings.wsgi.application'

AUTH_USER_MODEL = 'generic.Usuario'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

## databases settings
database_settings = os.path.join(BASE_DIR, 'settings/databases.py')
execfile(database_settings)


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#Static
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
PRODUCT_ROOT = 'products-img'