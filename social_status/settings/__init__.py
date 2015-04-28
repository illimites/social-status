from django.core.exceptions import ImproperlyConfigured

try:
    # Try to import local_settings module. It must be created by the person setting up the application.
    from .local_settings import *
except ImportError as exception:
    message = "'local_settings' module is missing. Please configure the application before running it."
    raise ImproperlyConfigured(message) from exception

if 'ENVIRONMENT' not in vars():
    message = "'local_settings' module does not define the 'ENVIRONMENT' setting."
    raise ImproperlyConfigured(message)
