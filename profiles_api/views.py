from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloAPIView(APIView):
    """HELLO API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        data = [
            'data1',
            'data2',
            'data3'
        ]

        return Response({'message': 'OK', 'list': data})

    def post(self, request):
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

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """TEST API View set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'create',
            'retrieve',
            'update',
            'partial_update',
            'destory'
        ]

        return Response({'message': 'Hello', 'viewset': a_viewset})

    def create(self, request):
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
        """Handle getting object by its ID"""
        return Response({'http_method': 'GET', 'pk': pk })

    def update(self, request, pk=None):
        """Handle updating object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of object"""
        return Response({'http_method': 'PATCH'})

    def destory(self, request, pk=None):
        """Deleting an object"""
        return Response({'http_method': 'DELETE'})
