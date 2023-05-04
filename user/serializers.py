from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    first_name = serializers.CharField(max_length=45)    
    user_name = serializers.CharField(max_length=45)
    about = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "user_name", "password", "first_name", 'about']

    def validate(self, attrs):
        email_exists = CustomUser.objects.filter(email=attrs["email"]).exists()
        user_name_exists = CustomUser.objects.filter(user_name=attrs["user_name"]).exists()
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


# class CurrentUserPostsSerializer(serializers.ModelSerializer):
#     posts = serializers.HyperlinkedRelatedField(
#         many=True, view_name="post_detail", queryset=CustomUser.objects.all()
#     )

#     class Meta:
#         model = CustomUser
#         fields = ["id", "username", "email", "posts"]