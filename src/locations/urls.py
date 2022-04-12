from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'api/address', AddressViewSet)
router.register(r'api/city', CityViewSet)

urlpatterns = [
]
urlpatterns += router.urls
