"""
Models to define the data structure for the backend.
"""

# Base Imports
import secrets

# Third Party Imports
from django.db import models


class BaseModel(models.Model):
    """ Common fields across the City and WeatherData models. """
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.CharField(max_length=60, null=True)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.CharField(max_length=60, null=True)


class City(BaseModel):
    """ Model representing city data. """

    name = models.CharField(max_length=60, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class WeatherData(BaseModel):
    """ Model representing weather data for a linked city and the provided date time. """

    date_time = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField(null=True)
    humidity = models.IntegerField(null=True)
    wind_speed = models.FloatField(null=True)
    precipitation = models.FloatField(null=True)

    def save(self, *args, **kwargs):
        """
        Precipitation comes in as a probability.
        Convert this here to a percentage as more intuitive on the front end.
        """
        if self.precipitation is not None:
            self.precipitation = self.precipitation * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Weather data for {self.city.name} at {self.date_time}."


class APIUser(models.Model):
    """
    Model for setting up an API Key.
    Only intended to be used by the developer when setting the application.

    To get API KEY follow these steps from a terminal.

        - manage.py shell
        - from backend.models import APIUser
        - api_user = APIUser.objects.create(name='your name')
        - print(api_user.api_key)

    """

    name = models.CharField(max_length=40, unique=True)
    api_key = models.CharField(max_length=24, unique=True, editable=False)

    def save(self, *args, **kwargs):
        """ API KEY is a computed field. """
        if not self.api_key:
            self.api_key = secrets.token_hex(12)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
