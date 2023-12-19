from django.urls import path
from .views import LocationListCreateView,index,loc

urlpatterns = [
    path('locations/', LocationListCreateView.as_view(), name='LocationListCreateView'),
    path('',index,name='index'),
    path('loc/<int:id>',loc,name="loc")
    # Add other URL patterns as needed
]
