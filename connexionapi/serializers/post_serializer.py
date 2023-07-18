from rest_framework import serializers
from connexionapi.models import Post
from connexionapi.serializers import ConnexionUserSerializer


class PostSerializer(serializers.ModelSerializer):
    """Serializes the swapper model to convert it to useable json"""
    connexion_user = ConnexionUserSerializer()
    class Meta:
        model = Post
        fields = ('id', 'body', 'image', 'connexion_user')
        