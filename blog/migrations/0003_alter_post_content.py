# Generated by Django 5.0.6 on 2024-05-26 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_tag_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
