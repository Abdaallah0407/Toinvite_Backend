from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import APIEventsViewSet

router = routers.DefaultRouter()
router.register('api/events', APIEventsViewSet, 'events')
urlpatterns = [
    path('', include(router.urls)),
]