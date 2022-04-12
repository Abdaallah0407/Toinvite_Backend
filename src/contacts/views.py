from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from .serializers import BackCallSerializer
from rest_framework.response import Response
# Create your views here.
class BackCallApi(generics.GenericAPIView):
    serializer_class = BackCallSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)