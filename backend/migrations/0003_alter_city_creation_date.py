# Generated by Django 4.2.4 on 2023-08-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_cities_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
