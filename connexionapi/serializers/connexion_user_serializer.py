from rest_framework import serializers
from connexionapi.models import ConnexionUser
from .connexion_friend_serializer import ConnexionFriendSerializer


class ConnexionUserSerializer(serializers.ModelSerializer):
    """Serializes the swapper model to convert it to useable json"""
    friends=ConnexionFriendSerializer(many=True)
    class Meta:
        model = ConnexionUser
        fields = ('id', 'user', 'bio','profile_picture', 'full_name', 'gender', 'orientation', 'friends')
        