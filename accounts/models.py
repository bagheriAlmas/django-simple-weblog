from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    email = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(blank=True, upload_to='avatars', null=True)
