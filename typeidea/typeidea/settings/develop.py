# flake8: NOQA

from .base import *

DEBUG = True

# DATABASES = {
# 'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'develop',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}