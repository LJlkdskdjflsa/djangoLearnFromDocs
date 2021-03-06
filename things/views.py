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
from rest_framework import viewsets, filters, generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import (
    SAFE_METHODS,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    BasePermission,
    IsAdminUser,
    DjangoModelPermissions,
)
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


# 之後要獨立程一個app
class PostUserWritePermission(BasePermission):
    message = "Edit the Post is restricted to the owner only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # can only access self data
        return obj.owner == request.user


class ThingList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ThingSerializer

    def get_queryset(self):
        try:
            user = self.request.user
            # staff can see all
            if user.is_staff:
                return Thing.objects.all()
            # normal user can only get his
            return Thing.objects.filter(owner=user)
        except:
            return Thing.objects.all()


class ThingDetail(generics.ListAPIView):
    serializer_class = ThingSerializer

    def get_queryset(self):
        slug = self.request.query_params.get("slug", None)
        print(slug)
        return Thing.objects.filter(slug=slug)


class ThingListDetailfilter(generics.ListAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^slug"]

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's ThinggreSQL backend.)
    # '$' Regex search.


class ThingSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^slug"]


"""class CreateThing(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer"""


class CreateThing(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # to support multipart html data
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        # print(request.data)
        serializer = ThingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminThingDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class EditThing(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ThingSerializer
    queryset = Thing.objects.all()


class DeleteThing(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ThingSerializer
    queryset = Thing.objects.all()


# Category


class CategoriesList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Define custome queryset
    def get_queryset(self):
        return Category.objects.all()

    # Define custome get object
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("_id")
        return get_object_or_404(Thing, slug=item)
