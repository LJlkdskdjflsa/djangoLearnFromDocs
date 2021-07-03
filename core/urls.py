from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("things/", include("things.urls"), name="things"),
    path("auth/", include("rest_framework.urls"), name="rest_framework"),
]
