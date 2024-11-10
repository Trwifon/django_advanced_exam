from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    email = models.EmailField(
        unique=True,
    )

    bio = models.TextField()

    avatar = models.URLField(
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
