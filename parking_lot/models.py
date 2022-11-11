from django.db import models

# Create your models here.



class Customer(models.Model):

    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return f"{self.name}"


class Parkinglot(models.Model):

    name = models.CharField(max_length=90)
    max_slot = models.IntegerField(default=1)
    availiable = models.IntegerField(default=0)
    parked = models.IntegerField(default=0)
    customer = models.ManyToManyField(Customer)
    qr_link = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return f"{self.name} have ({self.availiable})"