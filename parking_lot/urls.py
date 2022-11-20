from django.contrib import admin
from django.urls import path ,include
from . import views

app_name = 'parking_lot'
urlpatterns = [
    path('mypark', views.parkinglot_list, name='list'),
    path('<int:id>', views.info, name='info'),
    path('<int:id>/booking/', views.booking, name='booking'),
    path('create/',views.createParking,name='create'),
    path('<int:id>/qr/',views.one_button_book,name='one_button_book'),
    path('logout/',views.one_button_logout,name='one_button_logout'),
    path('<int:id>/checkout',views.checkout,name='checkout'),
    path('delete/<int:id>',views.deleteData,name='delete'),
    path('exit/',views.exit,name='exit'),
    path('',views.index,name='index'),
    path('ready/',views.onpark,name='onpark')
   
]