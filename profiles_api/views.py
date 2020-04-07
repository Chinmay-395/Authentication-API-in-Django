from django.shortcuts import render
# from rest_framework.views import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profiles_api.serializers import HelloSerializer, UserProfileSerializer
from profiles_api import models
from profiles_api import permissions
# Create your views here.


class HelloApiView(APIView):
    """ Test API view """
    serializer_class = HelloSerializer  # HelloSerializer
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

        serializer = HelloSerializer(data=request.data)
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
        """ Handle a partial partial_ of an object """
        return Response({'method': 'PATCATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    """ Action performed on typical API is done here """
    """ This is a METHOD provided by DRF """

    serializer_class = HelloSerializer

    def list(self, request):
        """ Return Hello message """
        a_viewset = [
            'Uss actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using ROuters',
            'PRovides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """ create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({'httpmethod': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating part an object """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle Destroying an object """
        return Response({'http_method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
