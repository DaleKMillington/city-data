# Third Party Imports
from django.contrib import admin

# Application Imports
from .models import (
    City,
    WeatherData
)

admin.site.register(City)
admin.site.register(WeatherData)
