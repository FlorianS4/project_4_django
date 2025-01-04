# Generated by Django 4.2.17 on 2025-01-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecrit_post', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='post_field',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='post_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='youtube_link',
            field=models.URLField(default=False, max_length=300),
        ),
    ]
