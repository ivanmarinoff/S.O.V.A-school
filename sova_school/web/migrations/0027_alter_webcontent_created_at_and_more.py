# Generated by Django 4.2.2 on 2023-07-30 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0026_alter_webcontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webcontent",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 30, 14, 14, 30, 52840)
            ),
        ),
        migrations.AlterField(
            model_name="webcontent",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 30, 14, 14, 30, 52840)
            ),
        ),
    ]
