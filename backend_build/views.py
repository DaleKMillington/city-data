# Base Imports
from concurrent.futures import ThreadPoolExecutor

# Third Party Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Application Imports
from backend.authentication import APIKeyAuthentication
from .owm_request import OpenWeatherMapRequest
from backend.models import (
    City,
    WeatherData
)
from backend.serializers import WeatherDataSerializer
from django.conf import settings
from .exceptions import (
    APIInternalServerError,
    OWMException
)


class BackendBuildView(APIView):
    authentication_classes = [APIKeyAuthentication]

    def get(self, request, *args, **kwargs):
        cities = City.objects.all()

        try:
            with ThreadPoolExecutor() as executor:
                results = list(executor.map(self._fetch_owm_data, cities))
                flattened_results = [item for sublist in results for item in sublist]
                self._create_weather_data_bulk(flattened_results)
        except OWMException as err:
            raise APIInternalServerError(f'Could not fetch weather data. Exception: {repr(err)}.')
        except ValidationError as err:
            raise APIInternalServerError(f'Could not create weather data. Exception: {repr(err)}.')

        return Response({"Detail": "Success."}, status=status.HTTP_200_OK)

    @staticmethod
    def _fetch_owm_data(city):
        owm = OpenWeatherMapRequest(
            api_token=settings.OPEN_WEATHER_MAP_API_KEY,
            city=city
        )
        data = owm.get_data()
        return data

    def _create_weather_data_bulk(self, results):
        serializer = WeatherDataSerializer(data=results, many=True, context={'request': self.request})
        if serializer.is_valid():
            WeatherData.objects.all().delete()
            serializer.save()
        else:
            raise ValidationError(serializer.errors)
