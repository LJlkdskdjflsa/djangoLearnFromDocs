from rest_framework import generics

from .models import Category, Thing
from .serializers import ThingSerializer, CategorySerializer
from rest_framework.permissions import (
    BasePermission,
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
    SAFE_METHODS,
)
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# 之後要獨立程一個app
class PostUserWritePermission(BasePermission):
    message = "Edit the Post is restricted to the owner only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # can only access self data
        return obj.owner == request.user


class CategoriesListlView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoriesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ThingsList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

    # Define custome queryset
    def get_queryset(self):
        return Thing.objects.all()

    # Define custome get object
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Thing, slug=item)


# replace with viewsets
"""
class ThingsListlView(generics.ListCreateAPIView, IsAuthenticatedOrReadOnly):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingsDetailView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
"""
