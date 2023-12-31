# Generated by Django 5.0a1 on 2023-10-08 14:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Level_1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("text", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("image_url", models.URLField(blank=True, null=True)),
                (
                    "file",
                    models.FileField(
                        blank=True, default=None, null=True, upload_to="files"
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True, default=None, null=True, upload_to="videos"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Content",
        ),
    ]
