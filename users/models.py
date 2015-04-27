from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # We want a custom user model from the beginning so that it's easy to customize later
    # and we are definitely going to want to customize it.
    pass
