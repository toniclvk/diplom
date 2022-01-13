from rest_framework.serializers import ModelSerializer

from my_project.models import Weather


class WeatherSerializer(ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
