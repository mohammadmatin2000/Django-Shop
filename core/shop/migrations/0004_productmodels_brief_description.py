# Generated by Django 4.2 on 2025-07-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_productcategorymodels_productmodels_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodels",
            name="brief_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
