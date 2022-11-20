from django import forms
from django.forms import ModelForm
from .models import *


class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','tel']


class createParkingLotForm(ModelForm):
    class Meta:
        model = Parkinglot 
        fields = ['name','max_slot','lat','lon']

"""
class slotForm(forms.Form):
    select = forms.CharField(label='Slot', max_length=100)

class slotForm(ModelForm):
    class Meta:
        model = Slot
        fields = ['who','name']
"""