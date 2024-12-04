# Generated by Django 5.0.4 on 2024-11-23 10:16

import FisherPoint.validators.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(4), FisherPoint.validators.validators.username_validator]),
        ),
    ]