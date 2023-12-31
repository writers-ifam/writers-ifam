# Generated by Django 3.2 on 2023-10-06 03:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('writers', '0006_auto_20231005_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='saved_poems', to=settings.AUTH_USER_MODEL),
        ),
    ]
