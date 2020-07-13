from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    def get(self,request,format=None):
        """Returns a list of API View features"""
        an_apiview=[
        'Uses HTTP Methods as functions(get,post,put,patch,delete)'
        'It is similar to a traditional Django view'
        'gives you most control over logic'
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
