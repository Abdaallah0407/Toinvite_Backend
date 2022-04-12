from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import  CategorySerializers
# Create your views here.

class APICategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get_queryset(self):
        queryset = Category.objects.order_by('title')

        return queryset