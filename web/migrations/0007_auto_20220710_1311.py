# Generated by Django 3.2.6 on 2022-07-10 10:11

import django.core.validators
from django.db import migrations, models
import web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dweet',
            name='body',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(400)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(30), web.validators.only_letters_validator], verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(30), web.validators.only_letters_validator], verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(30), web.validators.only_letters_and_numbers_validator], verbose_name='username'),
        ),
    ]
