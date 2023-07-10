from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from connexionapi.models import ConnexionUser
from connexionapi.serializers import ConnexionUserSerializer


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
            connexion_user = ConnexionUser.objects.get(pk=pk)
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