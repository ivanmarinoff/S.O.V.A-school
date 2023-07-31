# Generated by Django 4.2.2 on 2023-07-31 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("content", "0054_remove_content_content_type_remove_content_object_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="useranswers",
            name="content_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="content.content",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="useranswers",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
