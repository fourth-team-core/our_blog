# Generated by Django 4.1 on 2022-08-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0002_alter_bloguserprofile_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloguserprofile",
            name="avatar",
            field=models.ImageField(
                blank=True, upload_to="user_avatars", verbose_name="avatar"
            ),
        ),
    ]
