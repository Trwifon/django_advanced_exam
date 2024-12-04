# Generated by Django 5.0.4 on 2024-11-28 19:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_message_body'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]