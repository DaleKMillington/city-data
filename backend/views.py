# Third Party Imports
from rest_framework import viewsets
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
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [APIKeyAuthentication]


class WeatherDataView(APIView):
    authentication_classes = [APIKeyAuthentication]

    @staticmethod
    def get(request, city_name: str, *args, **kwargs):
        weather_data = WeatherData.objects.filter(city__name=city_name)
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)
