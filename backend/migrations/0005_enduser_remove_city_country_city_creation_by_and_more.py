# Generated by Django 4.2.4 on 2023-08-18 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_city_last_update_alter_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('creation_by', models.CharField(max_length=60, null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.CharField(max_length=60, null=True)),
                ('name', models.CharField(max_length=40)),
                ('api_key', models.CharField(editable=False, max_length=24, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.AddField(
            model_name='city',
            name='creation_by',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='last_update_by',
            field=models.CharField(max_length=60, null=True),
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
