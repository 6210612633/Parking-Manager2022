from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Parkinglot, Customer
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .form import * 
from django.urls import reverse
from requests import get 
import json

# Create your views here.

def one_button_book(request,id):
    parking = Parkinglot.objects.get(id=id)
    parking_lat = parking.lat
    parking_lon = parking.lon
    location = get("http://ip-api.com/json")
    location = location.json()
    location_lat = location["lat"]
    location_lon = location["lon"]
    print(parking_lat)
    
    print("result",parking_lat-location_lat)
    cond = 0
    if(0 <= parking_lat-location_lat <= 3):
        cond=1
    
    print(type(location))
    return render(request, 'parkinglot/one_button_page.html',{'lat':location_lat,'lon':location_lon,'status':cond})


def parkinglot_list(request):
    # Query all posts
    owned_park = Parkinglot.objects.all()
    print(owned_park)
    ### test
    
    return render(request, 'parkinglot/home.html', {'owned_park': owned_park})


def info(request,id):
    parkinglot = Parkinglot.objects.get(id=id)
    #cus = get_object_or_404(Parkinglot, id=id).customer
    #cus = cus.values()

    slot = Slot.objects.filter(parking=parkinglot)
    
    return render(request, 'parkinglot/park_info.html',{"slot":slot})

def about(request):
    return HttpResponse("About Page")

def createParking(request):
    
    if request.method == 'POST':
        form = createParkingLotForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            max_slot = request.POST['max_slot']
            newPark = Parkinglot.objects.create(name=name,max_slot=max_slot,availiable=max_slot)
            #form.save()
            i=1
            while i <= int(max_slot):
                Slot.objects.create(parking=newPark,name=f"parking #{i}")
                i = i + 1   
            return HttpResponseRedirect(reverse("parking_lot:list"))
    else:
        form = createParkingLotForm()
    return render(request, 'parkinglot/create_park.html', {'form': form})


def booking(request,id):
    free = get_object_or_404(Parkinglot, id=id).max_slot
    parking = Parkinglot.objects.get(id=id)
    slot = Slot.objects.filter(parking=parking,status=True)
    box = []
    for i in slot:
        box.append(i)
        print("dddd",i)
    x = box[0]
    setStatus = Slot.objects.filter(id=x.id)
    setStatus.update(status=False)
    print(x)
    if request.method == 'POST':
        owned_park = Parkinglot.objects.get(id=id)

        form = customerForm(request.POST, request.FILES)
    
        if form.is_valid():
            name = request.POST["name"]
            tel = request.POST["tel"]
            c = Customer.objects.create(name=name,tel=tel,slot=x)
            #owned_park.customer.add(c)
            owned_park.save()
            #form.save()
            return HttpResponseRedirect(reverse("parking_lot:list"))
    else:
        form = customerForm()
        
    return render(request, 'parkinglot/booking.html', {'form': form,'id':id})
    

"""
def view_status(request):
    slot = []
    if 0 < Parkinglot.max_slot:
        pass
    Customer = Parkinglot.objects.values_list('customer')
    return render(request, 'parkinglot/home.html',{"customer": Customer})
    
"""