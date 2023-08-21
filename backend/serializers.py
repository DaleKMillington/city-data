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

    @staticmethod
    def validate_forbidden_fields(data):
        forbidden_fields = ['creation_date', 'creation_by', 'last_update', 'last_update_by']
        for field in forbidden_fields:
            if field in data:
                raise serializers.ValidationError(f"The field '{field}' is not allowed in the payload.")
        return data

    def validate(self, data):
        return self.validate_forbidden_fields(data)

    def create(self, validated_data):
        api_key = self.context['request'].META.get('HTTP_X_API_KEY')
        api_user = APIUser.objects.get(api_key=api_key)
        validated_data['creation_by'] = api_user.name
        validated_data['last_update_by'] = api_user.name
        return super().create(validated_data)

    def update(self, instance, validated_data):
        api_key = self.context['request'].META.get('HTTP_X_API_KEY')
        api_user = APIUser.objects.get(api_key=api_key)
        validated_data['last_update_by'] = api_user.name
        return super().update(instance, validated_data)


class CitySerializer(BaseSerializer):
    class Meta:
        model = City
        fields = '__all__'

    @staticmethod
    def validate_latitude(value):
        if value < -90 or value > 90:
            raise serializers.ValidationError('Latitude must be between -90 and 90.')
        return value

    @staticmethod
    def validate_longitude(value):
        if value < -180 or value > 180:
            raise serializers.ValidationError('Longitude must be between -180 and 180.')
        return value


class WeatherDataSerializer(BaseSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
