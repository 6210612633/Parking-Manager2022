from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Parkinglot, Customer
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .form import * 
from django.urls import reverse
# Create your views here.


def parkinglot_list(request):
    # Query all posts
    owned_park = Parkinglot.objects.all()
    print(owned_park)
    return render(request, 'parkinglot/home.html', {'owned_park': owned_park})


def info(request,id):
    
    tr = get_object_or_404(Parkinglot, id=id).customer
    cu = tr.values()
    
    return render(request, 'parkinglot/park_info.html',{"customer": cu})

def about(request):
    return HttpResponse("About Page")


def booking(request,id):
    owned_park = Parkinglot.objects.get(id=id)
    print(owned_park.availiable)
    slot = []
    i = 1
    while i <= owned_park.availiable:
        slot.append(f"parking #{i}")
        i = i + 1

    if request.method == 'POST':
        form = customerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("parking_lot:booking"))
    else:
        form = customerForm()
    return render(request, 'parkinglot/booking.html', {'form': form,'ava':owned_park.availiable,'slot':slot})
    

"""
def view_status(request):
    slot = []
    if 0 < Parkinglot.max_slot:
        pass
    Customer = Parkinglot.objects.values_list('customer')
    return render(request, 'parkinglot/home.html',{"customer": Customer})
    
"""