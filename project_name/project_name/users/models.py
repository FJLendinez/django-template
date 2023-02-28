from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None # To delete the field username in abstract model
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
