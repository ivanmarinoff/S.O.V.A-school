# Generated by Django 4.2.2 on 2023-07-31 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("global_content", "0051_alter_globalcontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="globalcontent",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 31, 8, 48, 49, 729815)
            ),
        ),
        migrations.AlterField(
            model_name="globalcontent",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 31, 8, 48, 49, 729815)
            ),
        ),
    ]
