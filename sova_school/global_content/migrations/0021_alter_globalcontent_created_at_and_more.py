# Generated by Django 4.2.2 on 2023-07-30 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("global_content", "0020_alter_globalcontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="globalcontent",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 30, 9, 19, 26, 462969)
            ),
        ),
        migrations.AlterField(
            model_name="globalcontent",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 30, 9, 19, 26, 462969)
            ),
        ),
    ]
