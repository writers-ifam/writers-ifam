# Generated by Django 3.2 on 2023-11-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0007_alter_poem_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='books/cover/%Y/%m/%d/'),
        ),
    ]
