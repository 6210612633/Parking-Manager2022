from django.db import models

# Create your models here.






class Parkinglot(models.Model):

    name = models.CharField(max_length=90)
    max_slot = models.IntegerField(default=1)
    availiable = models.IntegerField(default=0)
    parked = models.IntegerField(default=0)
    #customer = models.ManyToManyField(Customer)
    qr_link = models.CharField(max_length=200,null=True, blank=True)
    lat = models.FloatField(default=0.00)
    lon = models.FloatField(default=0.00)
    
    

    def __str__(self):
        return f"{self.name} have ({self.availiable})"

class Slot(models.Model):

    parking = models.ForeignKey(Parkinglot,on_delete=models.CASCADE)
    name = models.CharField(null=True,max_length=10)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} have ({self.status})"


class Customer(models.Model):

    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=10,null=True)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.name}"
