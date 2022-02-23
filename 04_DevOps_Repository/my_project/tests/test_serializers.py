from django.test import TestCase
from my_project.models import Weather
from my_project.serializers import WeatherSerializer


class WeatherSerializerTestCase(TestCase):
    def test_ok(self):
        weather_1 = Weather.objects.create(id_field='5374758255329280',
                                           weather_state_name='Snow',
                                           wind_direction_compass='S',
                                           created='2022-01-01T22:10:56.863323Z',
                                           applicable_date='2022-01-01',
                                           min_temp='1',
                                           max_temp='3',
                                           the_temp='2'
                                              )
        weather_2 = Weather.objects.create(id_field='5374758255329281',
                                           weather_state_name='Snow',
                                           wind_direction_compass='S',
                                           created='2022-01-01T22:11:56.863323Z',
                                           applicable_date='2022-01-01',
                                           min_temp='0',
                                           max_temp='2',
                                           the_temp='1'
                                            )
        data = WeatherSerializer([weather_1, weather_2], many=True).data
        #print(data)
        expected_data = [
            {'id': weather_1.id,
             'id_field': '5374758255329280',
             'weather_state_name': 'Snow',
             'wind_direction_compass': 'S',
             'created': '2022-01-01T22:10:56.863323Z',
             'applicable_date': '2022-01-01',
             'min_temp': '1',
             'max_temp': '3',
             'the_temp': '2'
             },
            {'id': weather_2.id,
             'id_field': '5374758255329281',
             'weather_state_name': 'Snow',
             'wind_direction_compass': 'S',
             'created': '2022-01-01T22:11:56.863323Z',
             'applicable_date': '2022-01-01',
             'min_temp': '0',
             'max_temp': '2',
             'the_temp': '1'
             },
        ]
        #print(expected_data)

        self.assertEqual(expected_data, data)
