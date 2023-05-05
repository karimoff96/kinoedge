from .models import Studio
from rest_framework import serializers


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = "__all__"
