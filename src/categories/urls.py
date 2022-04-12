from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import APICategoryView


router = routers.DefaultRouter()
router.register('api/categories', APICategoryView, "categories")


urlpatterns = [
    path('', include(router.urls)),
]
