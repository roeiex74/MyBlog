# Generated by Django 5.0.6 on 2024-06-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_image_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog/images'),
        ),
    ]
