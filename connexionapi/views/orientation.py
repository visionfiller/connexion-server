from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from connexionapi.models import Orientation
from connexionapi.serializers import OrientationSerializer


class OrientationView(ViewSet):
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
            orientation = Orientation.objects.get(pk=pk)
            serializer = OrientationSerializer(orientation)
            return Response(serializer.data)
        except Orientation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all properties

        Returns:
            Response -- JSON serialized list of properties
        """
        orientations = Orientation.objects.all()
        serializer = OrientationSerializer(orientations, many=True)
        return Response(serializer.data)
