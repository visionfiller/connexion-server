from rest_framework import serializers
from connexionapi.models import Orientation


class OrientationSerializer(serializers.ModelSerializer):
    """Serializes the swapper model to convert it to useable json"""
    class Meta:
        model = Orientation
        fields = ('id', 'label')
        