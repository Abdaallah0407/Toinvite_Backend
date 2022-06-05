from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import EventsDetailSerializer, EventsListSerializer
from django.db.models import F
from rest_framework import status
from src.accounts.models import User

# Create your views here.


class APIEventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EventsListSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return EventsListSerializer
        if self.action == "retrieve" or self.action == "update":
            return EventsDetailSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Events.objects.all().order_by('title')
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
