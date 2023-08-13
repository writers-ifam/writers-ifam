# Generated by Django 4.2.4 on 2023-08-13 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("writers", "0002_author_is_published"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="", upload_to="book/cover/%Y/%m/%d/"
                    ),
                ),
                ("is_published", models.BooleanField(default=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="writers.author"
                    ),
                ),
            ],
        ),
    ]
