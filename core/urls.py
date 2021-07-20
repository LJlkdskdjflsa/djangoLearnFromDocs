from django.contrib import admin
from django.urls import path, include

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

# from things.admin import things_site
# from users.admin import user_site


urlpatterns = [
    # OAuth
    path("auth/", include("drf_social_oauth2.urls", namespace="drf")),
    # project management
    path("admin/", admin.site.urls),
    # the custome admin.site
    # path("things/admin/", things_site.urls),
    # path("users/admin/", user_site.urls),
    # OAuth provider
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    # app functions
    path("things/", include("things.urls"), name="things"),
    # user
    path("user/", include("users.urls"), name="users"),
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# admin.site.index_title = "The Things"
# admin.site.site_header = "The Things Admin"
# admin.site.site_title = "Things"
