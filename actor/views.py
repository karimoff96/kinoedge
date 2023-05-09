from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ActorSerializer
from django.shortcuts import render
from rest_framework import status
from .models import Actor, Major
from movie.models import Genre


# Create your views here.
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



