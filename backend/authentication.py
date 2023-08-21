"""
Class for custom API authentication.
"""

# Base Imports
from typing import Tuple

# Third Party Imports
from rest_framework import authentication
from rest_framework import exceptions

# Application Imports
from .models import APIUser
from city_data.exceptions import APIBadRequest


class APIKeyAuthentication(authentication.BaseAuthentication):
    """
    Custom authentication class to be used for all exposed APIs.
    Ensures the request header contains an X-API-KEY with value matching
    an api_key value from the APIUser model.
    """

    def authenticate(self, request) -> Tuple[APIUser, None]:
        api_key = request.META.get('HTTP_X_API_KEY')
        if not api_key:
            raise APIBadRequest('X-API-KEY not provided in header.')
        try:
            api_user = APIUser.objects.get(api_key=api_key)
        except APIUser.DoesNotExist:
            raise exceptions.AuthenticationFailed(f'Invalid API Key provided: {api_key}.')
        return api_user, None
