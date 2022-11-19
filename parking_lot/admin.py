from django.contrib import admin
from .models import Parkinglot , Customer , Slot
# Register your models here.

class TimeSlotAdmin(admin.ModelAdmin):
    readonly_fields = ('start','end')

admin.site.register(Slot,TimeSlotAdmin)

admin.site.register(Parkinglot)
admin.site.register(Customer)
#admin.site.register(Slot)