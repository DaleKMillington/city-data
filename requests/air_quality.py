"""
Class for handling requests to the air quality API
"""

# Base Imports
import requests
import logging
from enum import Enum

# Third Party Imports


# Application Imports
from django.conf import settings


class AirQualityRequest:

    def __init__(self):
        token: str = settings.BREEZO_API_KEY

    def get_city(self):
        pass
