# Generated by Django 4.2.17 on 2025-01-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecrit_post', '0010_post_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_private',
        ),
        migrations.AddField(
            model_name='post',
            name='alt_image',
            field=models.CharField(default='', max_length=100),
        ),
    ]
