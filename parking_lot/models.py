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
        return f"{self.name} have ({self.availiable}) id = {self.id}"


class Customer(models.Model):

    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return f"{self.name}"


class Slot(models.Model):

    parking = models.ForeignKey(Parkinglot,on_delete=models.CASCADE)
    name = models.CharField(null=True,max_length=10)
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    start = models.TimeField(auto_now=True,auto_now_add=False)
    end = models.TimeField(auto_now=True,auto_now_add=False)
    
    def __str__(self):
        return f"{self.parking} slot {self.name} status ({self.status}) slotID= {self.id}"