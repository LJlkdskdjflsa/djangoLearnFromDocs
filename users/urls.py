from django.urls import path
from .views import CustomUserCreate

urlpatterns = [
    path("create/", CustomUserCreate.as_view(), name="create_user"),
    # path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
    #      name='blacklist')
]
