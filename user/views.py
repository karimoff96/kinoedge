from .serializers import (
    SignUpSerializer,
    ChangePasswordSerializer,
    EmailVerificationSerializer,
    LoginSerializer,
)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, logout
from .tokens import create_jwt_pair_for_user
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SignUpAPIView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {"message": "User Created Successfully", "data": serializer.data}
            user = CustomUser.objects.get(email=request.data["email"])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_link = reverse("email-verify")

            abs_url = "http://" + current_site + relative_link + "?token=" + str(token)
            email_body = f"Hi {user.user_name}! Use the link below to verify your email:\n{abs_url}"

            data = {
                "email_body": email_body,
                "to_email": user.email,
                "email_subject": "Verify your email",
            }

            Util.send_email(data)
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        "token",
        in_=openapi.IN_QUERY,
        description="Description",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(
                jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"]
            )
            user = CustomUser.objects.get(id=payload["user_id"])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response(
                data={"email": "Successfully activated"}, status=status.HTTP_200_OK
            )

        except jwt.ExpiredSignatureError as error:
            return Response(
                {"error": "Activation link expired "},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except jwt.exceptions.DecodeError as error:
            return Response(
                {"error": "Invalid token "}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = CustomUser.objects.get(email=serializer.data["email"])
        if obj.is_staff:
            authority = "ADMIN"
        else:
            authority = "USER"
        data = {
            "user_name": obj.user_name,
            "email": obj.email,
            "first_name": obj.first_name,
            "start_date": obj.start_date,
            "about": obj.about,
            "is_staff": authority,
            "tokens": create_jwt_pair_for_user(obj),
        }
        return Response(data=data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"msg": "Successfully Logged out"}, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
