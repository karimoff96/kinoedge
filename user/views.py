from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from rest_framework.response import Response
from .serializers import SignUpSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser


class SignUpAPIView(APIView):
    def get(self, request):
        news = CustomUser.objects.all()
        serializer = SignUpSerializer(instance=news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "User Created Successfully", "data": serializer.data}
            print(response)
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = []

    def post(self, request):
        obj = CustomUser.objects.get(email=email)
        email = request.data.get("email")
        password = request.data.get("password")
        data = {
            "user_name": obj.user_name,
            "first_name": obj.first_name,
            "start_date": obj.start_date,
            "about": obj.about,
            "is_staff": obj.is_staff,
        }
        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login Successfull", "token": tokens, "user": data}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)
