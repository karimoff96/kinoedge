from .serializers import NewsSerializer, ActorSerializer, CategorySerializer, GenreSerializer
from .models import News, Tag, Actor, Genre, Major, Category
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


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


class ActorListAPIView(APIView):
    def get(self, request):
        news = Actor.objects.all()
        serializer = ActorSerializer(instance=news, many=True)
        return Response(serializer.data)

    def post(self, request):
        genres = request.data.get("genre").split()
        statuses = request.data.get("status").split()
        all_genres = []
        all_status = []
        for gen in genres:
            try:
                gen_obj = Genre.objects.get(name=gen)
                all_genres.append(gen_obj.id)
            except:
                gen_obj = Genre.objects.create(name=gen)
                all_genres.append(gen_obj.id)
        for stat in statuses:
            try:
                stat_obj = Major.objects.get(name=stat)
                all_status.append(stat_obj.id)
            except:
                stat_obj = Major.objects.create(name=stat)
                all_status.append(stat_obj.id)

        data = {
            "name": request.data.get("name"),
            "brief_info": request.data.get("brief_info"),
            "birth_place": request.data.get("birth_place"),
            "status": all_status,
            "citizenship": request.data.get("citizenship"),
            "career": request.data.get("career"),
            "genre": all_genres,
            "information": request.data.get("information"),
        }
        serializer = ActorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorDetailAPIView(APIView):
    def get_object(self, actor_id):
        try:
            return Actor.objects.get(id=actor_id)
        except Actor.DoesNotExist:
            return None

    def get(self, request, actor_id):
        actor_isntance = self.get_object(actor_id)
        if not actor_isntance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ActorSerializer(actor_isntance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, actor_id):
        actor_isntance = self.get_object(actor_id)
        if not actor_isntance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        genres = request.data.get("genre").split()
        statuses = request.data.get("status").split()
        all_genres = []
        all_status = []
        for gen in genres:
            try:
                gen_obj = Genre.objects.get(name=gen)
                all_genres.append(gen_obj.id)
            except:
                gen_obj = Genre.objects.create(name=gen)
                all_genres.append(gen_obj.id)
        for stat in statuses:
            try:
                stat_obj = Major.objects.get(name=stat)
                all_status.append(stat_obj.id)
            except:
                stat_obj = Major.objects.create(name=stat)
                all_status.append(stat_obj.id)

        data = {
            "name": request.data.get("name"),
            "brief_info": request.data.get("brief_info"),
            "birth_place": request.data.get("birth_place"),
            "status": all_status,
            "citizenship": request.data.get("citizenship"),
            "career": request.data.get("career"),
            "genre": all_genres,
            "information": request.data.get("information"),
        }
        serializer = ActorSerializer(instance=actor_isntance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, actor_id):
        actor_isntance = self.get_object(actor_id)
        if not actor_isntance:
            return Response(
                {"res": "Object with news id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        actor_isntance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)


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