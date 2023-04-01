from datetime import timedelta
from decouple import config


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}


ACCESS_TOKEN_LIFETIME = timedelta(minutes=5)
REFRESH_TOKEN_LIFETIME = timedelta(days=1)
ROTATE_REFRESH_TOKENS = False
BLACKLIST_AFTER_ROTATION = True

ALGORITHM = 'HS256'

AUTH_HEADER_TYPES = ['Bearer']
USER_ID_FIELD = 'id'
USER_ID_CLAIM = 'user_id'

AUTH_TOKEN_CLASSES = ['rest_framework_simplejwt.tokens.AccessToken']
TOKEN_TYPE_CLAIM = 'token_type'

SLIDING_TOKEN_LIFETIME = timedelta(minutes=5)
SLIDING_TOKEN_REFRESH_LIFETIME = timedelta(days=1)
