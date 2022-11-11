from django.contrib import admin
from django.urls import path ,include
from . import views

app_name = 'parking_lot'
urlpatterns = [
    path('', views.parkinglot_list, name='list'),
    path('<int:id>', views.info, name='info'),
    path('<int:id>/booking/', views.booking, name='booking'),
   
]