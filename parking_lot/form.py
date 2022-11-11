from django import forms
from django.forms import ModelForm
from .models import *


class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','tel']


