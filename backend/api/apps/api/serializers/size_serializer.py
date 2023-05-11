from rest_framework import serializers
from ..models import Sizes


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = ('id', 'description', 'height', 'diameter', 'tare')
