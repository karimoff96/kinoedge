from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Studio
from .serializers import StudioSerializer


class StudioListAPIView(APIView):
    def get(self, request):
        news = Studio.objects.all()
        serializer = StudioSerializer(instance=news, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            "name": request.data["name"],
            "founder_name": request.data["founder_name"],
            "location": request.data["location"],
            "product_types": request.data["product_types"],
            "employee_count": request.data["employee_count"],
            "history": request.data["history"],
            "profit": request.data["profit"],
            "page": request.data["page"],
            "capital": request.data["capital"],
            "award": request.data["award"],
            "news": request.data["news"],
        }
        serializer = StudioSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudioDetailAPIView(APIView):
    def get_object(self, studio_id):
        try:
            return Studio.objects.get(id=studio_id)
        except Studio.DoesNotExist:
            return None

    def get(self, request, studio_id):
        studio_instance = self.get_object(studio_id)
        if not studio_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = StudioSerializer(studio_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, studio_id):
        studio_instance = self.get_object(studio_id)
        if not studio_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data["name"],
            "founder_name": request.data["founder_name"],
            "location": request.data["location"],
            "product_types": request.data["product_types"],
            "employee_count": request.data["employee_count"],
            "history": request.data["history"],
            "profit": request.data["profit"],
            "page": request.data["page"],
            "capital": request.data["capital"],
            "award": request.data["award"],
            "news": request.data["news"],
        }
        serializer = StudioSerializer(instance=studio_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, studio_id):
        studio_instance = self.get_object(studio_id)
        if not studio_instance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        studio_instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
