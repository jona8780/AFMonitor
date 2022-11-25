from django.urls import path
from . import views

app_name = 'AFMonitor'
urlpatterns = [
    path("", views.home, name="home"),
    #path("arrivals", views.arrivals, name="arrivals"),
    #path("departures", views.departures, name="departures"),
    #path("weather", views.weather, name="weather"),
]
