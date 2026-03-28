from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from course_project_api import serializers
from course_project_api import models
from course_project_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create,retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello massage"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello and welcome {name} !'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):  # it retrieves an object based on it primary key
        """Handle getting the object based on the pk"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object like the http method put"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating the specific part of the object like http method Patch"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle deleting an object using its primary key """
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.ProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginView(ObtainAuthToken):
    """Handle authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """To handle the profile feed items including creating, updating and reading"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('status_text',)

    def perform_create(self, serializer):
        """Create the profile to the loggedin user"""
        serializer.save(user_profile=self.request.user)
