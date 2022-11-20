import requests, json, urllib.request
from bs4 import BeautifulSoup

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(
        request,
        'Afmonitor/index.html'
    )

def arrivals(request):

    URL = "https://www.toronto-pearson-airport.com/pearson-arrivals.php"
    array = BeautifulSoup(requests.get(URL).content, "html.parser").find("tbody").find_all("tr", class_="")
    flights = []
    for item in array:
        flight = item.find_all('td')
        data = []
        for item in flight:
            x = item.text.strip()
            data.append(x)
        flights.append(data)
    return render(
        request,
        'Afmonitor/arrivals.html',
        {
            'flights': flights
        }
    )
# Create your views here.
def departures(request):

    URL = "https://www.toronto-pearson-airport.com/pearson-departures.php"
    array = BeautifulSoup(requests.get(URL).content, "html.parser").find("tbody").find_all("tr", class_="")
    flights = []
    for item in array:
        flight = item.find_all('td')
        data = []
        for item in flight:
            x = item.text.strip()
            data.append(x)
        flights.append(data)
    return render(
        request,
        'Afmonitor/departures.html',
        {
            'flights': flights
        }
    )

def weather(request):

    API="S0sx8BspNrYA2N05NLvVOjnY5MbdRU9V"
    location="Lester B. Pearson International Airport"

    searchlocation="http://dataservice.accuweather.com/locations/v1/poi/search?apikey="+API+"&q="+location.replace(' ','%20')
    with urllib.request.urlopen(searchlocation) as searchlocation:
        data=json.loads(searchlocation.read().decode())
        locationkey=data[0]['Key']

    getforecast="http://dataservice.accuweather.com/currentconditions/v1/"+locationkey+"?apikey="+API+"&details=true"
    with urllib.request.urlopen(getforecast) as getforecast:
        data=json.loads(getforecast.read().decode())[0]

    return render(
        request,
        'Afmonitor/weather.html',
        {
            'weatherText': data['WeatherText'],
            'weatherIcon': data['WeatherIcon'],
            'temp': data['Temperature']['Metric']['Value'],
            'real': data['RealFeelTemperature']['Metric']['Value'],
            'windDegree': data['Wind']['Direction']['Degrees'],
            'windSpeed': data['Wind']['Speed']['Metric']['Value'],
            'windGust': data['WindGust']['Speed']['Metric']['Value'],
            'pressure': data['Pressure']['Imperial']['Value']
        }
    )