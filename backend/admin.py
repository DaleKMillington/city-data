# Third Party Imports
from django.contrib import admin

# Application Imports
from .models import (
    City,
    WeatherData,
    APIUser
)

admin.site.register(City)
admin.site.register(WeatherData)
admin.site.register(APIUser)