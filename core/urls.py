from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("things/", include("things.urls"), name="things"),
    path("auth/", include("rest_framework.urls"), name="rest_framework"),
    path("user/", include("users.urls"), name="users"),
    # simple jwt
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # verify HMAC-signed tokens without having access to your signing key
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # api docs
    path(
        "schema",
        get_schema_view(
            title="thingsAPI", description="API for the things", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path("docs/", include_docs_urls(title="ThingAPI")),
]
