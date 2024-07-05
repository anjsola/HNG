from django.shortcuts import render
from django.http import JsonResponse, request

def basic_api(request):
  if request.method == 'GET':
        visitor_ip = request.META.get('REMOTE_ADDR')
        visitor_name = request.GET.get('visitor_name', 'Mark')
        username = request.GET.get('username', None) 
        Location = "New York"

        #payload = {'ip': visitor_ip, 'format': 'json'}
        # api_result =  request.GET.get('https://api.ip2location.io/', None)
        # Location = api_result.json()
   
        # cityName = Location['city_name']

        # weather = request.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=3b6cb4536a3f0c99e3d357906ad951f9&units=metric'.format(cityName))
        # temps = weather.json()

        temperature = 11 #temps['main']['temp']
        greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees Celcius in {Location}"
        response_data = {
            "client_ip":visitor_ip,
            "location": Location,
            "greeting": greeting,
        }
  
  return JsonResponse(response_data)