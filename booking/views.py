from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer, Driver, Ride
from .serializers import CustomerSerializer, DriverSerializer, RideSerializer
from .utils.fare_calculator import calculate_fare 

# API for Customers
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# API for Drivers
class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

# API for Rides
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


    # API Endpoint for fare calculation
    @action(detail=False, methods=['POST'])
    def calculate_fare(self, request):
        """
        API Endpoint to calculate fare based on distance.
        Example JSON request body:
        {
            "distance_km": 10
        }
        """
        distance_km = request.data.get('distance_km', 0)

        try:
            fare = calculate_fare(float(distance_km))
            return Response({"distance_km": distance_km, "fare": fare})
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
        

