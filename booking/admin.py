from django.contrib import admin
from .models import Customer, Driver, Ride

# Register Models
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Ride)
