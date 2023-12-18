from django.urls import path
from .views import LocationListCreateView

urlpatterns = [
    path('locations/', LocationListCreateView.as_view(), name='LocationListCreateView'),
    # Add other URL patterns as needed
]
