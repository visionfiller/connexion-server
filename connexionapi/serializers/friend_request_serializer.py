from rest_framework import serializers
from connexionapi.models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):
    """Serializes the swapper model to convert it to useable json"""
    class Meta:
        model = FriendRequest
        fields = ('id', 'connexion_user_to', 'connexion_user_from', 'status')
        