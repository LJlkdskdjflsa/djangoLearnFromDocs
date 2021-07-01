from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from . import views

app_name = "things"

urlpatterns = [
    # path("upload_file", csrf_exempt(views.upload_file), name="upload_file"),
    path("<int:pk>/", views.ThingsDetailView.as_view(), name="detail-create"),
    path("", views.ThingsListlView.as_view(), name="list-create"),
    path(
        "category/<int:pk>/", views.CategoriesDetailView.as_view(), name="detail-create"
    ),
    path("category", views.CategoriesListlView.as_view(), name="list-create"),
]
