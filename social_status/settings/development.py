from .base import *

ENVIRONMENT = 'development'

DEBUG = True

SECRET_KEY = 'ob5i#m4xys_hjhr+!m#-7)vpoum!83q%76bdf9nd9ndw+y22#_'

TIME_ZONE = 'Europe/Warsaw'

# Keep at least one entry on this list in development because otherwise you won't see
# your custom e-mains to admins printed to the console.
ADMINS = (
    ('admin1', 'admin1@example.com'),
    ('admin2', 'admin2@example.com'),
)
MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'social-status@example.com'
SERVER_EMAIL       = DEFAULT_FROM_EMAIL
