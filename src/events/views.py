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
        queryset = Events.objects.filter(admin=self.request.user).order_by('title')
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if data.get('location'):
            data['location'] = Address.objects.create(name=data['location'], numeration=1).id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
