from django.core.validators import MinLengthValidator
from django.db import models

from FisherPoint.account.models import User


class Room(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(6)],
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    created_at= models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    host = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    participants = models.ManyToManyField(
        to=User,
        related_name='participants',
        blank=True,
    )

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name

