from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from course_project_api import serializers


class HelloApiView(APIView):
    """Test the APIView"""
    serializer_class = serializers.HelloSerializer  # whenever you get put, patch, delete expect a field called name with a max length of 10

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as (get, post, put, patch, delete )',
            'is similar to traditional Django View',
            'Gives you the most control over your logic',
            'is mapped manually to your URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of the object"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message': 'DELETE'})
