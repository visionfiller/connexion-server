from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from connexionapi.models import ConnexionUser, Gender, Orientation, FriendRequest
from connexionapi.serializers import ConnexionUserSerializer, FriendRequestSerializer


class ConnexionUserView(ViewSet):
    """ConnexionUserView"""

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
            connexion_user = ConnexionUser.objects.get(user=pk)
            serializer = ConnexionUserSerializer(connexion_user)
            return Response(serializer.data)
        except ConnexionUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all properties

        Returns:
            Response -- JSON serialized list of properties
        """
        connexion_users = ConnexionUser.objects.all()
        connexion_user = ConnexionUser.objects.get(user=request.auth.user)
        serializer = ConnexionUserSerializer(connexion_users, many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def my_profile(self, request):
        """Get the current user's properties"""
        try:
            connexion_user = ConnexionUser.objects.get(user=request.auth.user)
            serializer = ConnexionUserSerializer(connexion_user)
            return Response(serializer.data)
        except ConnexionUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PUT'], detail=False)
    def update_profile(self, request):
        """Get the current user's properties"""
        try:
            connexion_user = ConnexionUser.objects.get(user=request.auth.user)
            connexion_user.bio = request.data['bio']
            connexion_user.profile_picture = request.data['profile_picture']
            gender = Gender.objects.get(pk=request.data['gender'])
            connexion_user.gender = gender
            orientation = Orientation.objects.get(
                pk=request.data['orientation'])
            connexion_user.orientation = orientation
            connexion_user.save()
            serializer = ConnexionUserSerializer(connexion_user)
            return Response(serializer.data)
        except ConnexionUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=True)
    def send_friend_request(self, request, pk):
        """sends a request to the user to be added as a friend"""
        try:
            connexion_user_from = ConnexionUser.objects.get(
                user=request.auth.user)
            connexion_user_to = ConnexionUser.objects.get(user=pk)
            friend_request = FriendRequest.objects.create(
                connexion_user_from=connexion_user_from, connexion_user_to=connexion_user_to)
            friend_request.status = "Sent"
            friend_request.save()
            serializer = FriendRequestSerializer(friend_request)
            return Response(serializer.data)
        except ConnexionUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
