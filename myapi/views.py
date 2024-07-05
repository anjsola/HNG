from django.shortcuts import render
from django.http import JsonResponse, request
import requests

def basic_api(request):
  if request.method == 'GET':
        visitor_ip = request.META.get('REMOTE_ADDR')
        visitor_name = request.GET.get('visitor_name', 'Mark')
        if not visitor_name:
          return JsonResponse({'error': 'Missing visitor_name parameter'}, status=400)

        payload = {'ip': visitor_ip, 'format': 'json'}
        api_result =  requests.get('https://api.ip2location.io/', params = payload)
        location = api_result.json()
   
        cityName = location['city_name']

        weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=3b6cb4536a3f0c99e3d357906ad951f9&units=metric'.format(cityName))
        temps = weather.json()

        temperature = temps['main']['temp']
        greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees Celcius in {cityName}"
        response_data = {
            "client_ip":visitor_ip,
            "location": cityName,
            "greeting": greeting,
        }
  
  return JsonResponse(response_data)

