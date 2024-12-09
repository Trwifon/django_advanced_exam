from django.core.validators import MinLengthValidator
from django.db import models
from FisherPoint.account.models import User
from cloudinary.models import CloudinaryField

from FisherPoint.validators.validators import competition_title_validator, ValidateCloudinaryImage


class Competition(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(10, message='Title must be at least 10 characters'),
            competition_title_validator,
        ]
    )

    description = models.TextField(
        validators=[
            MinLengthValidator(100, message='Description must be at least 100 characters'),
        ]
    )

    photo = CloudinaryField(
        'image',
        null=True,
        blank=True,
        validators=[
            ValidateCloudinaryImage(0.5)
        ]
    )

    location = models.CharField(
        max_length=100,
        default=''
    )

    host = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='competitions',
    )

    participants = models.ManyToManyField(
        to=User,
    )

    date_of_event = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    first_place = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='first_place',
        null=True,
        blank=True,
    )

    second_place = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='second_place',
        null=True,
        blank=True,
    )

    third_place = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='third_place',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-date_of_event']
