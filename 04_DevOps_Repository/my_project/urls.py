from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('cleardb/', views.cleardb),
    path('importdb/', views.importdb),
   # path('importdb/', views.threading_job1),
    path('viewdb/', views.viewdb),
    path('about/', views.about)
]
