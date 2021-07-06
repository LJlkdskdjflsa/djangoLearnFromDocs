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
    # Thing Admin URLs
    path("admin/create/", views.CreateThing.as_view(), name="createThing"),
    path(
        "admin/edit/Thingdetail/<int:pk>/",
        views.AdminThingDetail.as_view(),
        name="admindetailThing",
    ),
    path("admin/edit/<int:pk>/", views.EditThing.as_view(), name="editThing"),
    path("admin/delete/<int:pk>/", views.DeleteThing.as_view(), name="deleteThing"),
]
