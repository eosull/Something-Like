# Generated by Django 4.2 on 2023-05-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="edited_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]