from .models import Movie, Genre, Category
from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(CountryFieldMixin,serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
