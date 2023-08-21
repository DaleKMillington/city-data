"""
API Views relating to the City and WeatherData models.
"""

# Third Party Imports
from rest_framework import (
    viewsets,
    status
)
from rest_framework.views import APIView
from rest_framework.response import Response

# Application Imports
from .models import (
    City,
    WeatherData
)
from .serializers import (
    CitySerializer,
    WeatherDataSerializer
)
from .authentication import APIKeyAuthentication


class CityViewSet(viewsets.ModelViewSet):
    """ View set to allow easy access to GET/POST/PATCH/PUT/DELETE via API. """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [APIKeyAuthentication]

    def create(self, request, *args, **kwargs):
        """ Allow a list of single element to be posted. """
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WeatherDataView(APIView):
    """ Weather data will only be requested via front-end. Therefore, custom view with only GET. """

    authentication_classes = [APIKeyAuthentication]

    @staticmethod
    def get(request, city_name: str, *args, **kwargs):
        weather_data = WeatherData.objects.filter(city__name=city_name)
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)
