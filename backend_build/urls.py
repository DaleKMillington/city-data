"""
URL conf for building the WeatherData. Designed to be triggered by a CRON process.
"""

# Third Party Imports
from django.urls import path

# Application Imports
from .views import BackendBuildView

urlpatterns = [
    path('', BackendBuildView.as_view()),
]
