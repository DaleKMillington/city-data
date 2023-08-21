"""
Models to define the data structure for the backend.
"""

# Base Imports
import secrets

# Third Party Imports
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.CharField(max_length=60, null=True)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.CharField(max_length=60, null=True)


class City(BaseModel):
    name = models.CharField(max_length=60, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class WeatherData(BaseModel):
    date_time = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField(null=True)
    humidity = models.IntegerField(null=True)
    wind_speed = models.FloatField(null=True)
    precipitation = models.FloatField(null=True)

    def save(self, *args, **kwargs):
        if self.precipitation is not None:
            self.precipitation = self.precipitation * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Weather data for {self.city.name} at {self.date_time}."


class APIUser(BaseModel):
    name = models.CharField(max_length=40)
    api_key = models.CharField(max_length=24, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = secrets.token_hex(12)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
