import os

import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.encoding import (
    DjangoUnicodeDecodeError,
    force_str,
    smart_bytes,
    smart_str,
)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic.edit import FormView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, response, status, views
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import (
    EmailVerificationSerializer,
    LoginSerializer,
    RegisterSerializer,
)

from .models import User
from .renderers import UserRenderer
from .serializers import (
    EmailVerificationSerializer,
    LoginSerializer,
    LogoutSerializer,
    RegisterSerializer,
    ResetPasswordEmailRequestSerializer,
    SetNewPasswordSerializer,
)
from .utils import Util


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get("APP_SCHEME"), "http", "https"]


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data["email"])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse("verify-email")
        absurl = "http://" + current_site + relativeLink + "?token=" + str(token)
        email_body = "Hi " + user.username + " Use the link below to verify your email \n" + absurl
        data = {"email_body": email_body, "to_email": user.email, "email_subject": "Verify your email"}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmailAPIView(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        "token", in_=openapi.IN_QUERY, description="Description", type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get("token")
        print(type(token))
        print(token)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({"email": "Successfully activated"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get("email", "")

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse("password-reset-confirm", kwargs={"uidb64": uidb64, "token": token})

            redirect_url = request.data.get("redirect_url", "")
            absurl = "http://" + current_site + relativeLink
            email_body = (
                "Hello, "
                + user.username
                + " \n Please use the link below to reset your password  \n"
                + absurl
                + "?redirect_url="
                + redirect_url
            )
            data = {"email_body": email_body, "to_email": user.email, "email_subject": "Reset your passsword"}
            Util.send_email(data)

        return Response({"success": "We have sent you a link to reset your password"}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        # redirect_url = request.GET.get("redirect_url")
        # print(redirect_url)
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            # covert to humen readable string
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                print("asdf")

                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url + "?token_valid=False")
                else:
                    return CustomRedirect(os.environ.get("FRONTEND_URL", "") + "?token_valid=False")
            return Response({"success": True, "message": "Credent Valid"})
            # print(redirect_url)
            # print(len(redirect_url))
            """if redirect_url and len(redirect_url) > 3:

                # success
                return CustomRedirect(
                    redirect_url + "?token_valid=True&message=Credentials Valid&uidb64=" + uidb64 + "&token=" + token
                )
            else:
                # print("asdf")

                return CustomRedirect(os.environ.get("FRONTEND_URL", "") + "?token_valid=False")"""

        except DjangoUnicodeDecodeError as identifier:
            try:
                # ?????
                if not PasswordResetTokenGenerator().check_token(user, token):
                    return CustomRedirect(redirect_url + "?token_valid=False")

            except UnboundLocalError as e:
                return Response(
                    {"error": "Token is not valid, please request a new one"}, status=status.HTTP_400_BAD_REQUEST
                )


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    # changing password use patch
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"success": True, "message": "Password reset success"}, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
