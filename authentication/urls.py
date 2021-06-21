from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("register", views.RegisterAPIView.as_view(), name="register"),
    path("login", views.LoginAPIView.as_view(), name="login"),
    path("logout/", views.LogoutAPIView.as_view(), name="logout"),
    path("verify-email", views.VerifyEmailAPIView.as_view(), name="verify-email"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("request-reset-email/", views.RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path("password-reset/<uidb64>/<token>/", views.PasswordTokenCheckAPI.as_view(), name="password-reset-confirm"),
    path("password-reset-complete", views.SetNewPasswordAPIView.as_view(), name="password-reset-complete")
    # path('user', views.AuthUserAPIView.as_view(), name='user'),
    # activate password
]
