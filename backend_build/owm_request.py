"""
Class for handling requests to Open Weather API.
"""

# Base Imports
from datetime import datetime

# Third Party Imports
import requests

# Application Imports
from backend.models import City
from city_data.exceptions import OWMException


class OpenWeatherMapRequest:

    def __init__(self, api_token: str, city: City):
        self.api_token: str = api_token
        self.city: City = city
        self.base_url: str = 'https://api.openweathermap.org/data/2.5/forecast?'

    def get_data(self) -> list:
        """ Attempt to retrieve and process the data from the Open Weather Map API. """
        try:
            url = f'{self.base_url}lat={self.city.latitude}&lon={self.city.longitude}&appid={self.api_token}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()['list']
        except requests.exceptions.HTTPError as err:
            raise OWMException(f"Open Weather Map raised a HTTPError. Exception: {repr(err)}.")
        except KeyError as err:
            raise OWMException(f"Open Weather Map response did not contain key 'list'. Exception: {repr(err)}.")
        return list(map(self._deconstruct_data, data))

    def _deconstruct_data(self, data: dict) -> dict:
        """ Safely deconstruct the data from Open Weather Map API. Some values might be omitted by design
        in response. For response details please see https://openweathermap.org/forecast5.
        """
        main = data.get('main')
        wind = data.get('wind')
        processed_data = {
            "date_time": datetime.utcfromtimestamp(data.get('dt')),
            "city": self.city.pk,
            "temperature": main.get('temp') if main else None,
            "humidity": main.get('humidity') if main else None,
            "wind_speed": wind.get('speed') if wind else None,
            "precipitation": data.get('pop')
        }
        return processed_data
