# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        return super(User, self).save(*args, **kwargs)
