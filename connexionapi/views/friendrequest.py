from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from connexionapi.models import FriendRequest, ConnexionUser
from connexionapi.serializers import FriendRequestSerializer


class FriendRequestView(ViewSet):
    """FriendRequestView"""

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
            friend_request = FriendRequest.objects.get(pk=pk)
            serializer = FriendRequestSerializer(friend_request)
            return Response(serializer.data)
        except FriendRequest.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all properties

        Returns:
            Response -- JSON serialized list of properties
        """
        friend_requests = FriendRequest.objects.all()
        serializer = FriendRequestSerializer(friend_requests, many=True)
        return Response(serializer.data)
    @action(methods=['GET'], detail=False)
    def myfriendrequests(self, request):
            """Get the current user's friend requests"""
            try:
                connexion_user = ConnexionUser.objects.get(user=request.auth.user)
                friend_requests = FriendRequest.objects.filter(connexion_user_to=connexion_user, status="Sent")
                serializer = FriendRequestSerializer(friend_requests, many=True)
                return Response(serializer.data)
            except ConnexionUser.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    @action(methods=['PUT'], detail=True)
    def approve(self, request,pk):
            """approve request"""
            try:
                connexion_user_to = ConnexionUser.objects.get(user=request.auth.user)
                friend_request = FriendRequest.objects.get(pk=pk,connexion_user_to=connexion_user_to, status="Sent")
                friend_request.status= "Approved"
                friend_request.save()
                return Response(None, status=status.HTTP_204_NO_CONTENT)
              
            except FriendRequest.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


