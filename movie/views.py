from .serializers import CategorySerializer, GenreSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Genre, Category
from rest_framework import status


class CategoryListAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(instance=category, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            "name": request.data.get("name"),
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def get(self, request, category_id):
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = CategorySerializer(category_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, category_id):
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data.get("name"),
        }
        serializer = CategorySerializer(instance=category_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        category_instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)

class GenreListAPIView(APIView):
    def get(self, request):
        news = Genre.objects.all()
        serializer = GenreSerializer(instance=news, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            "name": request.data.get("name"),
        }
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailAPIView(APIView):
    def get_object(self, genre_id):
        try:
            return Genre.objects.get(id=genre_id)
        except Genre.DoesNotExist:
            return None

    def get(self, request, genre_id):
        genre_instance = self.get_object(genre_id)
        if not genre_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GenreSerializer(genre_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, genre_id):
        genre_instance = self.get_object(genre_id)
        if not genre_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data.get("name"),
        }
        serializer = GenreSerializer(instance=genre_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, genre_id):
        genre_instance = self.get_object(genre_id)
        if not genre_instance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        genre_instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)