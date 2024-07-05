from django.shortcuts import render
from django.http import JsonResponse

def basic_api(request):
  if request.method == 'GET':
        visitor_ip = request.META.get('REMOTE_ADDR')
        visitor_name = request.GET.get('visitor_name', 'Mark')
        Location = "New York"

        temperature = 11
        greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees Celcius in {Location}"
        response_data = {
            "client_ip":visitor_ip,
            "location": Location,
            "greeting": greeting,
        }
  
  return JsonResponse(response_data)