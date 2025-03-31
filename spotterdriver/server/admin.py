from django.contrib import admin

from .models import Driver, Journey, Trailer, Trip, Truck

admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(Trailer)
admin.site.register(Trip)
admin.site.register(Journey)

# Register your models here.
