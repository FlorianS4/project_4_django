# Generated by Django 4.2.17 on 2025-01-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecrit_post', '0003_alter_post_options_rename_content_post_post_field_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_field',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
