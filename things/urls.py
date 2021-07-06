from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "things"

"""router = DefaultRouter()
router.register("", views.ThingsList, basename="thing")
router.register("category/", views.CategoriesList, basename="category")
urlpatterns = router.urls"""
urlpatterns = [
    path("detail/", views.ThingDetail.as_view(), name="detailcreate"),
    path("search/", views.ThingListDetailfilter.as_view(), name="thingsearch"),
    path("", views.ThingList.as_view(), name="listcreate"),
]
