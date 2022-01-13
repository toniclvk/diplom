from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Weather, DataView


# Register your models here.
@admin.register(Weather)
class WeatherAdmin(ModelAdmin):
    pass


admin.site.register(DataView)
