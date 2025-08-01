# Generated by Django 4.2 on 2025-07-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile/default.png",
                null=True,
                upload_to="profile/",
            ),
        ),
    ]
