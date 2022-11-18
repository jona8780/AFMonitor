import requests
from bs4 import BeautifulSoup

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("go to /arrivals")

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
