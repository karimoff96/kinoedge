from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import Studio
from .serializers import StudioSerializer


class StudioListAPIView(APIView):
    def get(self, request):
        news = Studio.objects.all()
        serializer = StudioSerializer(instance=news, many=True)
        return Response(serializer.data)
    
    def post(self, request):        
        data = {
            'name':request.data['name'],
            'founder_name':request.data['founder_name'],
            'location':request.data['location'],
            'product_types':request.data['product_types'],
            'employee_count':request.data['employee_count'],
            'history':request.data['history'],
            'profit':request.data['profit'],
            'page':request.data['page'],
            'capital':request.data['capital'],
            'award':request.data['award'],
            'news':request.data['news'],
        }
        serializer = StudioSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)