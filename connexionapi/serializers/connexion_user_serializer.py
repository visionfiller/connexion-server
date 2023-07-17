from rest_framework import serializers
from connexionapi.models import ConnexionUser


class ConnexionUserSerializer(serializers.ModelSerializer):
    """Serializes the swapper model to convert it to useable json"""
    class Meta:
        model = ConnexionUser
        fields = ('id', 'user', 'bio','profile_picture', 'full_name', 'gender', 'orientation')
        