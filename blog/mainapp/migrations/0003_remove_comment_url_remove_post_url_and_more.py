# Generated by Django 4.1 on 2022-08-11 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_alter_post_options_remove_comment_published_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="url",
        ),
        migrations.RemoveField(
            model_name="post",
            name="url",
        ),
        migrations.RemoveField(
            model_name="postcategory",
            name="url",
        ),
        migrations.RemoveField(
            model_name="tag",
            name="url",
        ),
    ]
