from rest_framework import serializers
from connexionapi.models import FriendRequest
from .connexion_friend_serializer import ConnexionFriendSerializer

class FriendRequestSerializer(serializers.ModelSerializer):
    """Serializes the swapper model to convert it to useable json"""
    connexion_user_from = ConnexionFriendSerializer(many=False)
    class Meta:
        model = FriendRequest
        fields = ('id', 'connexion_user_to', 'connexion_user_from', 'status')
        