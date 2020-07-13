from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
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
