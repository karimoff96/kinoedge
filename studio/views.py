from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from .serializers import StudioSerializer

class StudioListAPIView(APIView):
    def get(self, request):
        data = {
            'name':request.data['name'],
            'founder_name':request.data['founder_name'],
            'location':request.data['location'],
            'product_types':request.data['product_types'],
            'employee_count':request.data['employee_count'],
            'profit':request.data['profit'],
            'page':request.data['page'],
            'video':request.data['video'],
            'logo':request.data['logo'],
            'capital':request.data['capital'],
            'award':request.data['award'],
            'news':request.data['news'],
        }
