# Generated by Django 3.2.6 on 2022-06-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_dweet_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
