"""
Serializers relating to the City and WeatherData models.
"""

# Third Party Imports
from rest_framework import serializers

# Application Imports
from .models import (
    City,
    WeatherData,
    APIUser
)


class BaseSerializer(serializers.ModelSerializer):
    """ Common serializer functionality across the City and WeatherData models. """

    @staticmethod
    def validate_forbidden_fields(data):
        """ Prevent computed fields from being provided in the payload. """
        forbidden_fields = ['creation_date', 'creation_by', 'last_update', 'last_update_by']
        for field in forbidden_fields:
            if field in data:
                raise serializers.ValidationError(f"The field '{field}' is not allowed in the payload.")
        return data

    def validate(self, data):
        """ Main validate method to be picked up automatically by DRF. """
        return self.validate_forbidden_fields(data)

    def create(self, validated_data):
        """ On create actions compute the creation_by and last_update_by fields. """
        api_key = self.context['request'].META.get('HTTP_X_API_KEY')
        api_user = APIUser.objects.get(api_key=api_key)
        validated_data['creation_by'] = api_user.name
        validated_data['last_update_by'] = api_user.name
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """ On update actions compute the last_update_by fields. """
        api_key = self.context['request'].META.get('HTTP_X_API_KEY')
        api_user = APIUser.objects.get(api_key=api_key)
        validated_data['last_update_by'] = api_user.name
        return super().update(instance, validated_data)


class CitySerializer(BaseSerializer):
    """ Serializer for the City model. """
    class Meta:
        model = City
        fields = '__all__'

    @staticmethod
    def validate_latitude(value):
        """ Ensure provided latitude is a valid value. """
        if value < -90 or value > 90:
            raise serializers.ValidationError('Latitude must be between -90 and 90.')
        return value

    @staticmethod
    def validate_longitude(value):
        """ Ensure provided longitude is a valid value. """
        if value < -180 or value > 180:
            raise serializers.ValidationError('Longitude must be between -180 and 180.')
        return value


class WeatherDataSerializer(BaseSerializer):
    """
    Simple Serializer for the WeatherData model.
    Omits custom validations as data comes from Open Weather Map API.
    Hence, assume the data has already been validated on their end.
    """
    class Meta:
        model = WeatherData
        fields = '__all__'
