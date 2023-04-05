from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent.parent

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
