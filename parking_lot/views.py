from django.shortcuts import render
from django.http import HttpResponse
from .models import Parkinglot, Customer
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    Customer = Parkinglot.objects.all()
    tr = get_object_or_404(Parkinglot, id=1).customer
    cu = tr.values('name')
    print(tr.values('name'))
    return render(request, 'parkinglot/home.html',{"customer": cu})

def about(request):
    return HttpResponse("About Page")

"""
def view_status(request):
    slot = []
    if 0 < Parkinglot.max_slot:
        pass
    Customer = Parkinglot.objects.values_list('customer')
    return render(request, 'parkinglot/home.html',{"customer": Customer})
    
"""