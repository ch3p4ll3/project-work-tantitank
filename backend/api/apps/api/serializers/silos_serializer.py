from rest_framework import serializers
from ..models import Silos
from .liquids_serializer import LiquidsSerializer
from .size_serializer import SizesSerializer
from .sensors_in_silos_serializer import SensorsInSilosSerializer


class SilosSerializer(serializers.ModelSerializer):
    liquid = LiquidsSerializer(read_only=True)
    size = SizesSerializer(read_only=True)
    sensors = SensorsInSilosSerializer(source='sensorsinsilos_set', many=True, required=False)

    class Meta:
        model = Silos
        fields = ('id', 'name', 'size', 'liquid', 'sensors')
