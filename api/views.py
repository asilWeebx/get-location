from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['country', 'city','street']
    def post(self, request, *args, **kwargs):
        # Extract latitude and longitude from the request data
        city = request.data.get('city')
        country = request.data.get('country')
        more = request.data.get('more')
        street = request.data.get('street')
        zipcode = request.data.get('zipcode')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        # Create a new location entry
        Location.objects.create(latitude=latitude, longitude=longitude,city=city,country=country,more=more,street=street,zipcode=zipcode)

        return Response({'message': 'Location saved successfully!'}, status=status.HTTP_201_CREATED)


def index(request):
    location = Location.objects.all()


    ctx = {
        'location':location
    }


    return render(request,'index.html',ctx)

def loc(request,id):
    location = Location.objects.get(id=id)

    ctx = {
        'location':location
    }

    return render(request,'loc.html',ctx)