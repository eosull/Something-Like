# Generated by Django 4.2 on 2023-05-29 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_edited_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='edited_at',
        ),
    ]
