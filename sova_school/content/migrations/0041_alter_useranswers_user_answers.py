# Generated by Django 4.2.2 on 2023-07-30 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("content", "0040_remove_useranswers_id_alter_useranswers_user_answers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useranswers",
            name="user_answers",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
