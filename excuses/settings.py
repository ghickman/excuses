# Django settings for excuses project.
from os.path import abspath, dirname, join

DIRNAME = abspath(dirname(__file__))

ADMINS = (
    ('George Hickman', 'george@ghickman.co.uk'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'excuses',
    }
}

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'

SITE_ID = u'4f114eb3de8b650cff00001d'

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = join(DIRNAME, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(DIRNAME, 'static_media')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_DIRS = (join(DIRNAME, 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x8ami0$vzeyb-#$u*5$*7p8e_y*=_bjbj(2gcl^d)8ky=$t_7-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'excuses.urls'

TEMPLATE_DIRS = (
    join(DIRNAME, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'django_extensions',
    'django_mongodb_engine',
    'gunicorn',

    'core',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
