# from django.shortcuts import render
import requests
import datetime
import calendar

# Create your views here.
from django.forms import forms
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .forms import DataViewForm
from my_project.models import Weather, DataView
from my_project.serializers import WeatherSerializer
from datetime import datetime


class WeatherViewSet(ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['applicable_date', 'created']
    search_fields = ['applicable_date', 'created']
    ordering_fields = ['applicable_date', 'created']


def index(request):
    # context = ""  # {'all_info' : all_cities, 'form' : form}
    return render(request, "my_project/index.html")


def cleardb(request):
    url = 'http://127.0.0.1:8000/weather/'
    res = requests.get(url).json()
    info_records = len(res)

    if request.method == 'POST':

        for i in range(len(res)):
            url_del = 'http://127.0.0.1:8000/weather/{}/'
            # print("Result req id = ", res[i]["id"])
            x = requests.delete(url_del.format(res[i]["id"]))
            print("Result of delete", x)
        info_records_dels = len(res)
        res = requests.get(url).json()
        info_records = len(res)
        message = "Just deleted"
        message2 = "weather records."
        context = {'info': info_records, 'info2': info_records_dels, 'message': message, 'message2': message2}
        return render(request, "my_project/cleardb.html", context)

    if info_records == 0:
        message = "Nothing to delete"
        message2 = "weather records."
    else:
        message = "Are you sure you want to delete "
        message2 = "weather records ?"
    info_records_dels = 0
    context = {'info': info_records, 'info2': info_records_dels, 'message': message, 'message2': message2}
    return render(request, "my_project/cleardb.html", context)


def importdb(request):
    # appid = '3cd3cd1218efe2186fcc4541491f5338'
    url = 'https://www.metaweather.com/api/location/2122265/{}/'
    # date 2021/12/1
    # Date in the format yyyy/mm/dd. Most location have data from early 2013 to 5-10 days in the future
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    days_in_month = calendar.monthrange(currentYear, currentMonth)[1]

    # print("Year= ", currentYear, "Month= ", currentMonth)
    # print("Number days=", days_in_month)
    # data_test = "%s" % currentYear + "/" + "%s" % currentMonth + "/" + "01"
    # print("data_test=", data_test)
    if request.method == 'POST':
        url_clear = 'http://127.0.0.1:8000/weather/'
        res = requests.get(url_clear).json()
        for i in range(len(res)):
            url_del = 'http://127.0.0.1:8000/weather/{}/'
            # print("Result req id = ", res[i]["id"])
            x = requests.delete(url_del.format(res[i]["id"]))
        # allday_data_info = []

        for k in range(1, days_in_month + 1):
            data = "%s" % currentYear + "/" + "%s" % currentMonth + "/" + "%s" % k
            print("Data of request", data)
            res = requests.get(url.format(data)).json()

            for i in range(len(res)):
                data_info = {
                    'id_field': res[i]["id"],
                    'weather_state_name': res[i]["weather_state_name"],
                    'wind_direction_compass': res[i]["wind_direction_compass"],
                    'created': res[i]["created"],
                    'applicable_date': res[i]["applicable_date"],
                    'min_temp': res[i]["min_temp"],
                    'max_temp': res[i]["max_temp"],
                    'the_temp': res[i]["the_temp"],
                }
                # print("Data_info=", data_info)
                r = requests.post('http://127.0.0.1:8000/weather/', json=data_info)
                print("Upload request  ", r)
        res = requests.get('http://127.0.0.1:8000/weather/').json()
        info_records = len(res)
        context = {'info_imported': info_records}
        return render(request, "my_project/importdb.html", context)
        # allday_data_info.append(data_info)
    #    all_cities.append(city_info)
    info_records = 0
    context = {'info_imported': info_records}
    return render(request, "my_project/importdb.html", context)


def viewdb(request):
    url = 'http://127.0.0.1:8000/weather/?applicable_date={}&ordering=created'

    if (request.method == 'POST'):
        form = DataViewForm(request.POST)
        form.save()
        dates_views = DataView.objects.all()
        # print("lenght dates_views=", len(dates_views), "last element = ", dates_views[len(dates_views) - 1].data)
        data = dates_views[len(dates_views) - 1].data
        x = requests.get(url.format(data)).json()
        flag = 1
        form = DataViewForm()
        context = {'info_view': x, 'info_data': data, 'form': form, 'flag': flag}
        return render(request, "my_project/viewdb.html", context)

    form = DataViewForm()

    currentMonth = datetime.now().strftime('%m')
    currentYear = datetime.now().year
    currentDay = datetime.now().strftime('%d')
    data = "%s" % currentYear + "-" + "%s" % currentMonth + "-" + "%s" % currentDay
    print('currentYear= ', currentYear, ' currentMonth = ', currentMonth, 'currentDay = ', currentDay)
    print('data= ', data)
    # res = requests.get(url).json()
    x = requests.get(url.format(data)).json()
    flag = 0
    context = {'info_view': x, 'info_data': data, 'form': form, 'flag': flag}
    return render(request, "my_project/viewdb.html", context)


def about(request):
    url_clear = 'http://127.0.0.1:8000/weather/'
    res = len(requests.get(url_clear).json())
    context = {'info': res}
    return render(request, "my_project/about.html", context)
