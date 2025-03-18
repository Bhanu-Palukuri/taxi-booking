from rest_framework import serializers
from .models import Customer, Driver, Ride

# Serializer for Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # Include all fields

# Serializer for Driver
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

# Serializer for Ride
class RideSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='customer.name')  # Show customer name in API
    driver_name = serializers.ReadOnlyField(source='driver.name')  # Show driver name in API

    class Meta:
        model = Ride
        fields = '__all__'
