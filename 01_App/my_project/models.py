from django.db import models


# Create your models here.
class DataView(models.Model):
    # Pattern  YYYY-MM-DD 2022-01-09
    data = models.CharField(max_length=10)

    def __srt__(self):
        return self.data


class Weather(models.Model):
    # From API
    # id	                    integer	Internal identifier for the forecast
    # weather_state_name	    string  Text description of the weather state
    # wind_direction_compass	string	compass point	Compass point of the wind direction
    #
    # applicable_date	        date	Date that the forecast or observation pertains to
    #
    id_field = models.BigIntegerField()
    weather_state_name = models.CharField(max_length=20)
    wind_direction_compass = models.CharField(max_length=20)
    created = models.DateTimeField()
    applicable_date = models.DateField()
    min_temp = models.CharField(max_length=20)
    max_temp = models.CharField(max_length=20)
    the_temp = models.CharField(max_length=20)

    def __str__(self):
        return f'Id {self.id}:{self.created}'
