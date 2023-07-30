# Generated by Django 4.2.2 on 2023-07-30 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("content", "0039_alter_content_created_at_alter_content_updated_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useranswers",
            name="id",
        ),
        migrations.AlterField(
            model_name="useranswers",
            name="user_answers",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
