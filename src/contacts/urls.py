from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import  BackCallApi
router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('api/backcall', BackCallApi.as_view()),
]
