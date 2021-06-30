from rest_framework import generics

from .models import Category, Thing
from .serializers import ThingSerializer


class ThingsListlView(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    pass


class ThingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    pass
