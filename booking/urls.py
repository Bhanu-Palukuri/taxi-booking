from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, DriverViewSet, RideViewSet

# Router for automatically generating API URLs
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'rides', RideViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include API endpoints
    path('api/calculate-fare/', RideViewSet.as_view({'post': 'calculate_fare'})),
]
