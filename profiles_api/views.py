from django.shortcuts import render
# from rest_framework.views import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views here.


class HelloApiView(APIView):
    """ Test API view """
    serializer_class = serializers.HelloSerializer  # HelloSerializer
    """ it is a standard way to retrieve serilizer-class in view """

    def get(self, request, format=None):
        """ Returns a list of APIview features """
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)'
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name in it."""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # For a list of status-codes: http://www.django-rest-framework.org/api-guide/status-codes/  # noqa

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})
