# Generated by Django 4.2 on 2025-07-20 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0009_ordermodels_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ordermodels",
            name="payment",
        ),
    ]
