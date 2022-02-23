from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from my_project.models import Weather
from my_project.serializers import WeatherSerializer


class WeatherApiTestCase(APITestCase):
    def test_get(self):
        weather_1 = Weather.objects.create(id_field='5374758255329280',
                                           weather_state_name='Snow',
                                           wind_direction_compass='S',
                                           created='2022-01-01T22:10:56.863323Z',
                                           applicable_date='2022-01-01',
                                           min_temp='1',
                                           max_temp='3',
                                           the_temp='2')
        weather_2 = Weather.objects.create(id_field='5374758255329281',
                                           weather_state_name='Snow',
                                           wind_direction_compass='S',
                                           created='2022-01-01T22:11:56.863323Z',
                                           applicable_date='2022-01-01',
                                           min_temp='0',
                                           max_temp='2',
                                           the_temp='1')

        url = reverse('weather-list')
        response = self.client.get(url)
        serializer_data = WeatherSerializer([weather_1, weather_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
