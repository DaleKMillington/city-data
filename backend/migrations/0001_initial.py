# Generated by Django 4.2.4 on 2023-08-21 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('api_key', models.CharField(editable=False, max_length=24, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('creation_by', models.CharField(max_length=60, null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.CharField(max_length=60, null=True)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('creation_by', models.CharField(max_length=60, null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.CharField(max_length=60, null=True)),
                ('date_time', models.DateTimeField()),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.IntegerField(null=True)),
                ('wind_speed', models.FloatField(null=True)),
                ('precipitation', models.FloatField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.city')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
