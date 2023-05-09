from .models import Movie, Genre, News, Category
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
