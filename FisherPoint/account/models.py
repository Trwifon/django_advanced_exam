from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary.models import CloudinaryField
from FisherPoint.validators.validators import username_validator, ValidateCloudinaryImage


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(4), username_validator],
    )

    email = models.EmailField(
        unique=True
    )

    description = models.TextField()

    avatar = CloudinaryField(
        'image',
        null=True,
        blank=True,
        validators=[
            ValidateCloudinaryImage(0.5)
        ]
    )

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'
        return None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

