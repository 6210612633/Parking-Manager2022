
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Parkinglot, Customer
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .form import * 
from django.urls import reverse
from requests import get 
import json
from datetime import datetime

# Create your views here.

def one_button_logout(request):
    return render(request, 'parkinglot/one_button_logout.html')

def one_button_book(request,id):
    
    parking = Parkinglot.objects.get(id=id)
    parking_lat = parking.lat
    #parking_lon = parking.lon
    location = get("http://ip-api.com/json")
    location = location.json()
    location_lat = location["lat"]
    location_lon = location["lon"]

    print(id)
    print(location) 
    print(type(location))
    return render(request, 'parkinglot/one_button_page.html',{'lat':location_lat,'lon':location_lon,'id':id})


def parkinglot_list(request):
   
    owned_park = Parkinglot.objects.all()
    print(owned_park)

    return render(request, 'parkinglot/ownpark.html', {'owned_park': owned_park})


def info(request,id):
    parkinglot = Parkinglot.objects.get(id=id)
    park_lat = parkinglot.lat
    park_lon = parkinglot.lon
    name = parkinglot.name
    slot = Slot.objects.filter(parking=parkinglot)
    
    return render(request, 'parkinglot/park_info.html',{"slot":slot,"lat":park_lat,"lon":park_lon,"name":name})


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

    parking = Parkinglot.objects.get(id=id)
    slot = Slot.objects.filter(parking=parking,status=True)
    box = []
    if slot.exists(): #ถ้ามีที่จอดว่าง
        for i in slot:
            box.append(i)
            print("dddd",i)
    
        x = box[0] #slot แรกสุด
        if request.method == 'POST':
            owned_park = Parkinglot.objects.get(id=id)

            form = customerForm(request.POST, request.FILES)
            setStatus = Slot.objects.filter(id=x.id)
            
            if form.is_valid():
                name = request.POST["name"]
                tel = request.POST["tel"]
                c = Customer.objects.create(name=name,tel=tel)
                #owned_park.customer.add(c)
                print("pos2",x.id)
                
                setStatus.update(status=False)
                setStatus.update(customer=c)
                setStatus.update(start=datetime.now())
                print("SSS",setStatus)
                #owned_park.save()
                #form.save()
                return HttpResponseRedirect(reverse("parking_lot:onpark"))
        else:
            form = customerForm()
        return render(request, 'parkinglot/booking.html', {'form': form,'id':id ,'slot':x.name,"slotid":x.id})
    
    else: #ที่จอดรถเต็ม
        print("bae bae")
        return render(request, 'parkinglot/booking.html', {'status': "full"})



def checkout(request,id):
    slot = Slot.objects.get(id=id)
    timestart = slot.start
    timeend = slot.end
    timeend = datetime.now().time
    cus = slot.customer.id
    print(cus)
    fee = 500
    #slot = Slot.objects.filter(id=id).update(status=True)
    customer = Customer.objects.get(id=cus)
    #customer.delete()
    return render(request, 'parkinglot/checkout.html', {'start': timestart,'end':timeend,'customer':customer,'fee':fee,'slotnum':slot.id})

def deleteData(request,id):
    slot = Slot.objects.get(id=id)
    
    cus = slot.customer.id
    slot = Slot.objects.filter(id=id).update(status=True)
    customer = Customer.objects.get(id=cus)
    customer.delete()
    return HttpResponseRedirect(reverse("parking_lot:list"))

def index(request):
    parking = Parkinglot.objects.all()
    print(len(parking))
    return render(request, 'parkinglot/index.html',{'parking':parking,'len':len(parking)})


def exit(request):
    if request.method == 'POST':
        form = customerForm(request.POST, request.FILES)
        if form.is_valid():
            #name = request.POST['name']
            phone = request.POST['tel']
            cus = Customer.objects.get(tel=phone)
            slot  = Slot.objects.get(customer=cus)
            timestart = slot.start
            timeend = slot.end
            timeend = datetime.now().time
            print(cus)
            print(slot.id)
            #form.save()

            return render(request, 'parkinglot/checkout.html', {'start': timestart,'end':timeend,'customer':cus,'fee':500,'slotnum':slot.id})
    else:
        form = customerForm()
    return render(request, 'parkinglot/exit.html',{"form":form})

def onpark(request):
    return render(request, 'parkinglot/onpark.html')


""" BACKUP
    if request.method == 'POST':
        owned_park = Parkinglot.objects.get(id=id)

        form = customerForm(request.POST, request.FILES)
        setStatus = Slot.objects.filter(id=x.id)
        if form.is_valid():
            name = request.POST["name"]
            tel = request.POST["tel"]
            c = Customer.objects.create(name=name,tel=tel)
            #owned_park.customer.add(c)
            print("pos2",x.id)
            
            setStatus.update(status=False)
            setStatus.update(customer=c)
            print("SSS",setStatus)
            #owned_park.save()
            #form.save()
            return HttpResponseRedirect(reverse("parking_lot:list"))
    else:
        form = customerForm()
        
    return render(request, 'parkinglot/booking.html', {'form': form,'id':id ,'slot':x.name})
    


def view_status(request):
    slot = []
    if 0 < Parkinglot.max_slot:
        pass
    Customer = Parkinglot.objects.values_list('customer')
    return render(request, 'parkinglot/home.html',{"customer": Customer})
    
"""