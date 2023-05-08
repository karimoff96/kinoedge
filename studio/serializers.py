from .models import Studio
from rest_framework import fields, serializers
from .models import PRODUCT_TYPES

class StudioSerializer(serializers.ModelSerializer):
    product_types = fields.MultipleChoiceField(choices=PRODUCT_TYPES)
    class Meta:
        model = Studio
        fields = "__all__"
        