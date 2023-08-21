"""
URL confs relating to the City and WeatherData models.
"""

# Third Party Imports
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Application Imports
from .views import (
    CityViewSet,
    WeatherDataView
)

router = DefaultRouter()
router.register(r'city', CityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('weather/<str:city_name>/', WeatherDataView.as_view())
]
