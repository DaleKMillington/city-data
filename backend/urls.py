# Third Party Imports
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Application Imports
from .views import CityViewSet

router = DefaultRouter()
router.register(r'city', CityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
