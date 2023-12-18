from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def post(self, request, *args, **kwargs):
        # Extract latitude and longitude from the request data
        city = request.data.get('city')
        country = request.data.get('country')
        more = request.data.get('more')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        # Create a new location entry
        Location.objects.create(latitude=latitude, longitude=longitude,city=city,country=country,more=more)

        return Response({'message': 'Location saved successfully!'}, status=status.HTTP_201_CREATED)