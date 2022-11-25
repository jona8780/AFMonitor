import requests, json, urllib.request
from bs4 import BeautifulSoup

from django.shortcuts import render

def home(request):
    arrivals = farrivals()
    departures = fdepartures()
    weather = fweather()

    return render(
        request,
        'AFMonitor/index.html',
        {
            'arrivals': arrivals,
            'departures': departures,
            'weatherText': weather['WeatherText'],
            'weatherIcon': weather['WeatherIcon'],
            'temp': weather['Temperature']['Metric']['Value'],
            'real': weather['RealFeelTemperature']['Metric']['Value'],
            'windDegree': weather['Wind']['Direction']['Degrees'],
            'windSpeed': weather['Wind']['Speed']['Metric']['Value'],
            'windGust': weather['WindGust']['Speed']['Metric']['Value'],
            'pressure': weather['Pressure']['Imperial']['Value']

        }
    )

# def arrivals(request):
def farrivals():

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
    return flights
    # return render(
    #     request,
    #     'AFMonitor/arrivals.html',
    #     {
    #         'flights': flights
    #     }
    # )

# def departures(request):
def fdepartures():

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
    return flights
    # return render(
    #     request,
    #     'AFMonitor/departures.html',
    #     {
    #         'flights': flights
    #     }
    # )

# def weather(request):
def fweather():

    API="S0sx8BspNrYA2N05NLvVOjnY5MbdRU9V"
    location="Lester B. Pearson International Airport"

    searchlocation="http://dataservice.accuweather.com/locations/v1/poi/search?apikey="+API+"&q="+location.replace(' ','%20')
    with urllib.request.urlopen(searchlocation) as searchlocation:
        data=json.loads(searchlocation.read().decode())
        locationkey=data[0]['Key']

    getforecast="http://dataservice.accuweather.com/currentconditions/v1/"+locationkey+"?apikey="+API+"&details=true"
    with urllib.request.urlopen(getforecast) as getforecast:
        weather=json.loads(getforecast.read().decode())[0]

    return weather
    # return render(
    #     request,
    #     'AFMonitor/weather.html',
    #     {
    #         'weatherText': weather['WeatherText'],
    #         'weatherIcon': weather['WeatherIcon'],
    #         'temp': weather['Temperature']['Metric']['Value'],
    #         'real': weather['RealFeelTemperature']['Metric']['Value'],
    #         'windDegree': weather['Wind']['Direction']['Degrees'],
    #         'windSpeed': weather['Wind']['Speed']['Metric']['Value'],
    #         'windGust': weather['WindGust']['Speed']['Metric']['Value'],
    #         'pressure': weather['Pressure']['Imperial']['Value']
    #     }
    #)