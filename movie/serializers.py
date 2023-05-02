from .models import Major, Movie, Actor, Genre, Tag, News, Category, Studio, Image
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
