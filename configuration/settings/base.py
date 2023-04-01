from configuration.settings.middleware_settings import *  # noqa: ignore=F401 isort:skip
from configuration.settings.installed_apps_settings import *  # noqa: ignore=F401 isort:skip
from configuration.settings.internationalizations_settings import *  # noqa: ignore=F401 isort:skip
from configuration.settings.auth_settings import *  # noqa: ignore=F401 isort:skip
from configuration.settings.media_settings import *  # noqa: ignore=F401 isort:skip
from configuration.settings.database_settings import *  # noqa: ignore=F401 isort:skip
from configuration.settings.rest_framework_settings import *  # noqa: ignore=F401 isort:skip

from decouple import config

ALLOWED_HOSTS = []

DEBUG = config('DEBUG', default=False, cast=bool)

DJANGO_SETTINGS_MODULE = config('DJANGO_SETTINGS_MODULE')

ROOT_URLCONF = 'configuration.urls'

WSGI_APPLICATION = 'configuration.wsgi.application'