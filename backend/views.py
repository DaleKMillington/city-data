# Third Party Imports
from rest_framework import viewsets

# Application Imports
from .models import (
    City
)
from .serializers import CitySerializer
from .authentication import APIKeyAuthentication


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [APIKeyAuthentication]


