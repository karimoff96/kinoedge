from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NewsSerializer
from django.shortcuts import render
from rest_framework import status
from .models import News, Tag


# Create your views here.
class NewsListAPIView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(instance=news, many=True)
        return Response(serializer.data)

    def post(self, request):
        tags = request.data.get("tag").split()
        exists_tags = []
        for tag in tags:
            try:
                tag_obj = Tag.objects.get(name=tag)
                exists_tags.append(tag_obj.id)
            except:
                tag_obj = Tag.objects.create(name=tag)
                exists_tags.append(tag_obj.id)
        data = {
            "title": request.data.get("title"),
            "content": request.data.get("content"),
            "publication_date": request.data.get("publication_date"),
            "source": request.data.get("source"),
            "tag": exists_tags,
        }
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailAPIView(APIView):
    def get_object(self, news_id):
        try:
            return News.objects.get(id=news_id)
        except News.DoesNotExist:
            return None

    def get(self, request, news_id):
        news_instance = self.get_object(news_id)
        if not news_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = NewsSerializer(news_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, news_id):
        news_instance = self.get_object(news_id)
        if not news_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        tags = request.data.get("tag").split()
        exists_tags = []
        for tag in tags:
            try:
                tag_obj = Tag.objects.get(name=tag)
                exists_tags.append(tag_obj.id)
            except:
                tag_obj = Tag.objects.create(name=tag)
                exists_tags.append(tag_obj.id)
        data = {
            "title": request.data.get("title"),
            "content": request.data.get("content"),
            "publication_date": request.data.get("publication_date"),
            "source": request.data.get("source"),
            "tag": exists_tags,
        }
        serializer = NewsSerializer(instance=news_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, news_id):
        news_instance = self.get_object(news_id)
        if not news_instance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        news_instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
