from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser
from django.contrib import auth
from .tokens import create_jwt_pair_for_user


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    user_name = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "user_name", "password"]

    def validate(self, attrs):
        email_exists = CustomUser.objects.filter(email=attrs["email"]).exists()
        user_name_exists = CustomUser.objects.filter(
            user_name=attrs["user_name"]
        ).exists()
        if email_exists:
            raise ValidationError("This email is already in use")
        if user_name_exists:
            raise ValidationError("This username is already in use")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = CustomUser
        fields = ["token"]


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    user_name = serializers.CharField(max_length=68, min_length=6, read_only=True)
    tokens = serializers.CharField(max_length=500, min_length=6, read_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "user_name", "tokens"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials, try again")
        if not user.is_active:
            raise AuthenticationFailed("Account disaled, contact to admin")
        if not user.is_verified:
            raise AuthenticationFailed("Email is not verified")

        return {
            "email": user.email,
            "username": user.user_name,
            "tokens": create_jwt_pair_for_user(user),
        }
