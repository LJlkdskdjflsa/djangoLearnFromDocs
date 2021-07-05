from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "things"

router = DefaultRouter()
router.register("", views.ThingsList, basename="thing")
urlpatterns = router.urls

"""urlpatterns = [
    # path("upload_file", csrf_exempt(views.upload_file), name="upload_file"),
    path(
        "category/<int:pk>/",
        views.CategoriesDetailView.as_view(),
        name="detail-category-create",
    ),
    path("category", views.CategoriesListlView.as_view(), name="list-category-create"),
    # path("<int:pk>/", views.ThingsDetailView.as_view(), name="detail-create"),
    # path("", views.ThingsListlView.as_view(), name="list-create"),
]"""
