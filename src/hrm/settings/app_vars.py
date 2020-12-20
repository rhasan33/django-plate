import os

# django vars
AUTH_USER_MODEL = 'user.User'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
APPEND_SLASH = False
STATIC_URL = '/static/'

# env
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))

REDIS_HOST = os.environ.get('REDIS_HOST')
RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
# request setup
REQUEST_TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', 8))
