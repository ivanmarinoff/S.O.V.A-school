# Generated by Django 4.2.2 on 2023-08-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("global_content", "0008_alter_globalcontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="globalcontent",
            name="created_at",
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
        migrations.AlterField(
            model_name="globalcontent",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
