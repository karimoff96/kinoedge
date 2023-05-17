from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/", views.SignUpAPIView.as_view(), name="signup"),
    path("email-verify/", views.VerifyEmail.as_view(), name="email-verify"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "change-password/", views.ChangePasswordView.as_view(), name="change-password"
    ),
    path(
        "reset-password/",
        include("django_rest_passwordreset.urls", namespace="reset-password"),
    ),
]
