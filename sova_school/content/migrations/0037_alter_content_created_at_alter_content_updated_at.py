# Generated by Django 4.2.2 on 2023-07-29 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0036_alter_content_created_at_alter_content_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 29, 17, 41, 22, 485289)
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 29, 17, 41, 22, 485289)
            ),
        ),
    ]
