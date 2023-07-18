from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from connexionapi.models import Post, ConnexionUser
from connexionapi.serializers import PostSerializer


class PostView(ViewSet):
    """PostView"""

    def get_permissions(self):
        if self.request.method == 'GET':
            # AllowAny permission for GET requests
            return [AllowAny()]
        else:
            # IsAuthenticated permission for other methods (POST, PUT, DELETE)
            return [IsAuthenticated()]

    def retrieve(self, request, pk):
        """Handle GET requests for single property

        Returns:
            Response -- JSON serialized property
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all properties

        Returns:
            Response -- JSON serialized list of properties
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new product for the current user's store"""
        user = ConnexionUser.objects.get(user=request.auth.user)

        try:
            new_post = Post.objects.create(
                connexion_user= user,
                body= request.data['body'],
                image= request.data['image']
            )
            serializer = PostSerializer(new_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
