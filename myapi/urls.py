from django.urls import path
from . import views


urlpatterns = [
    path('', views.basic_api, name='basic_api'),
    path('api/hello/', views.basic_api),
]