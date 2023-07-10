from rest_framework import serializers
from connexionapi.models import Gender


class GenderSerializer(serializers.ModelSerializer):
    """Serializes the swapper model to convert it to useable json"""
    class Meta:
        model = Gender
        fields = ('id', 'label')
        