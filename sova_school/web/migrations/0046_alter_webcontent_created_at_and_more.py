# Generated by Django 4.2.2 on 2023-07-31 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0045_alter_webcontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webcontent",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 31, 8, 40, 34, 364093)
            ),
        ),
        migrations.AlterField(
            model_name="webcontent",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 31, 8, 40, 34, 364093)
            ),
        ),
    ]
