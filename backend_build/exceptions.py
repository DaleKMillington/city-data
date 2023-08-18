# Third Party Imports
from rest_framework import status
from rest_framework.exceptions import APIException


class APIInternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Internal server error.'
    default_code = 'internal_server_error'


class OWMException(Exception):
    pass
