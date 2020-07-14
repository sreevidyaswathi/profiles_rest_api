from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of API View features"""
        an_apiview=[
        'Uses HTTP Methods as functions(get,post,put,patch,delete)'
        'It is similar to a traditional Django view'
        'gives you most control over logic'
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
    def post(self,request):
         """ create a hello message with our name"""
         serializer=serializers.HelloSerializer(data=request.data )
         if(serializer.is_valid()):
             name=serializer.data.get('name')
             message='Hello{}!'.format(name)
             return Response({'message':message})
         else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        """ handles updating an object"""
        return Response({'method':'put'})
    def patch(self,request,pk=None):
        """Patch request,only updates fields provided in the request."""
        return Response({'method':'patch'})
    def delete(self,request,pk=None):
        """Deletes an object"""
        return Response({'method':'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View set"""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
         """return a hello message."""
         a_viewset = [
         'Uses actions (list,create,retrieve,update,partial_update)',
         'Automatically maps to URLs using routers'
         'Provides more functionality with less code'
         ]
         return Response({'message': 'Hello', 'a_view_set':a_viewset})
    def create(self,request):
        """create a new Hello message"""
        serializer =serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello{}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        """Handles getting an object by its ID"""
        return Response({'http_method':'GET'})
    def update(self,request,pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self,request,pk=None):
        """Handles updating part of an object"""
        return Response({'http_method':'PATCH'})
    def destroy(self,request,pk=None):
        """Handles removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles."""
    serializer_class=serializers.UserPofileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """check emails and passwords and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use ObtainAuthToken API view to validate and create a token"""
        return ObtainAuthToken().post(request)
