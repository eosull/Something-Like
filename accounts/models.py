from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    pass
    # Additional Fields go here

    def __str__(self):
        return self.username

    