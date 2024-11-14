from django.db import models
from FisherPoint.account.models import User
from FisherPoint.room.models import Room


class Message(models.Model):
    body = models.TextField()

    created_at= models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name='messages',
    )

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.body[0:100]

