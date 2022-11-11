from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   # path('/test',views.view_status,name='viewstatus')
]