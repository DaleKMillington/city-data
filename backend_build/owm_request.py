"""
Class for handling requests to Open Weather API
"""

# Base Imports
import logging
from datetime import datetime

# Third Party Imports
import requests

# Application Imports
from backend.models import City
from .exceptions import OWMException


class OpenWeatherMapRequest:

    def __init__(self, api_token: str, city: City):
        self.api_token = api_token
        self.city = city
        self.base_url = 'https://api.openweathermap.org/data/2.5/forecast?'

    def get_data(self) -> list:
        url = f'{self.base_url}lat={self.city.latitude}&lon={self.city.longitude}&appid={self.api_token}'
        response = requests.get(url)
        response.raise_for_status()
        try:
            data = response.json()['list']
        except KeyError as err:
            raise OWMException(f"Open Weather Map response did not contain key 'list'. Exception: {repr(err)}.")
        return list(map(self._deconstruct_data, data))

    def _deconstruct_data(self, data: dict) -> dict:
        main = data.get('main')
        wind = data.get('wind')
        processed_data = {
            "date_time": datetime.utcfromtimestamp(data.get('dt')),
            "city": self.city.pk,
            "temperature": main.get('temp', '') if main else '',
            "humidity": main.get('humidity', '') if main else '',
            "wind_speed": wind.get('speed', '') if wind else '',
            "precipitation": data.get('pop', '')
        }
        return processed_data
