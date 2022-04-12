from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from services.permissions import IsAdminOrReadOnly, IsAdmin

from .serializers import AddressSerializer, AddressUpdateCreateSerializer, CitySerializer, CityUpdateCreateSerializer
from src.locations.models import Address, City


class CityViewSet(ModelViewSet):
    queryset = City.objects.all().order_by('numeration')
    serializer_class = CitySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CityUpdateCreateSerializer
        else:
            return CitySerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all().order_by('numeration')
    serializer_class = AddressSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['city', ]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AddressUpdateCreateSerializer
        else:
            return AddressSerializer
