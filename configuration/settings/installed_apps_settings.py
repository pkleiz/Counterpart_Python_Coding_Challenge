BUSINESS_APPS = [
    'apps.usgs_earthquakes',
    'apps.cities',
    'apps.logs',
    'frontend'
]

THIRD_APPS = [
    'rest_framework',
    'rest_framework.authtoken'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + BUSINESS_APPS
