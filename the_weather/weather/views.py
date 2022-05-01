from django.shortcuts import render, HttpResponse
import requests
import json
from weather.models import  City

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4bb926de1b192aadaf082010b22c3fee'
	cities = City.objects.all()

	if request.method == 'POST':
		city_dropdown = request.POST['city-dropdown']
		try:
			city = City.objects.filter(id=city_dropdown).first()
			city_weather = requests.get(url.format(city)).json()#request the API data and convert the JSON to Python data types
			weather = {
			'city': city,
			'temperature': city_weather['main']['temp'],
			'description': city_weather['weather'][0]['description'],
			'icon' : city_weather['weather'][0]['icon']
			}

		except: pass
		context = {'weather': weather, 'cities':cities}
	else:
		context = {'cities':cities}
	return render(request, 'weather/index.html', context) #returns the index.html template
