from django.db import models
from django.utils.timezone import now  # Import timezone

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(default=now)  # Automatically set the timestamp

class Driver(models.Model):
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50, unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

class Ride(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    ride_status = models.CharField(
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed')],
        max_length=20,
        default='Pending'
    )
    created_at = models.DateTimeField(default=now)
