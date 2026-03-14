from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test the APIView"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as (get, post, put, patch, delete )',
            'is similar to traditional Django View',
            'Gives you the most control over your logic',
            'is mapped manually to your URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
