from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationListCreateView, index, loc, LocationViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')
urlpatterns = [
    path('locations/', LocationListCreateView.as_view(), name='LocationListCreateView'),
    path('',index,name='index'),
    path('api/', include(router.urls)),
    path('loc/<int:id>',loc,name="loc")
    # Add other URL patterns as needed
]
