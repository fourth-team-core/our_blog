# Generated by Django 4.1 on 2022-08-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0003_alter_bloguserprofile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloguserprofile",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="", verbose_name="avatar"),
        ),
    ]
