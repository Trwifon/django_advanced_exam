from django.db import models
from FisherPoint.account.models import User
from FisherPoint.competition.models import Competition
from FisherPoint.room.models import Room
from cloudinary.models import CloudinaryField


class Message(models.Model):
    body = models.TextField(
        verbose_name="Message",
    )

    created_at= models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_messages',
    )

    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name='room_messages',
    )

    image = CloudinaryField(
        'image',
        null=True,
        blank=True)

    likes = models.ManyToManyField(
        to=User,
        related_name='liked_messages',
        blank=True,
    )

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.body[0:100]


