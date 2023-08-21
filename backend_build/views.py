"""
API View for building the WeatherData. Designed to be triggered by a CRON process.
"""

# Base Imports
from concurrent.futures import ThreadPoolExecutor

# Third Party Imports
from django.db import transaction
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
from city_data.exceptions import (
    APIInternalServerError,
    OWMException
)


class BackendBuildView(APIView):
    """ Class that is responsible for building the Weather Data on a POST trigger. """

    authentication_classes = [APIKeyAuthentication]

    def post(self, request, *args, **kwargs):
        cities = City.objects.all()
        try:
            # For each record in the City model, open a dedicated thread to request the data.
            # This might encounter limiting issues imposed by Open Weather Map API if number of city records is large.
            with ThreadPoolExecutor() as executor:
                results = list(executor.map(self._fetch_owm_data, cities))
            flattened_results = [item for sublist in results for item in sublist]
            self._create_weather_data_bulk(flattened_results)
        except OWMException as err:
            raise APIInternalServerError(f'Could not fetch weather data. Exception: {repr(err)}.')
        except Exception as err:
            raise APIInternalServerError(f'Could not create weather data. Exception: {repr(err)}.')
        return Response({"Detail": "Success."}, status=status.HTTP_200_OK)

    @staticmethod
    def _fetch_owm_data(city) -> list:
        """ Callback to fetch Open Weather Map data for a given City instance. """
        owm = OpenWeatherMapRequest(
            api_token=settings.OPEN_WEATHER_MAP_API_KEY,
            city=city
        )
        data = owm.get_data()
        return data

    def _create_weather_data_bulk(self, results) -> None:
        """
        Checks weather data is valid via Serializer.

        If valid then the existing weather data is removed as this is forecast data.
        Hence, not interested in keeping historic data and more recent forecasts
        are likely to be more accurate.

        Finally, saves new weather data in a bulk operation.
        Serializer has already passed checks for all data so this operation should be safe.

        However, handled within atomic transaction just in-case bulk create fails and we are
        left with no data.
        """

        serializer = WeatherDataSerializer(data=results, many=True, context={'request': self.request})
        if serializer.is_valid():
            with transaction.atomic():
                try:
                    WeatherData.objects.all().delete()
                    serializer.save()
                except Exception as err:
                    raise err
        else:
            raise ValidationError(serializer.errors)
