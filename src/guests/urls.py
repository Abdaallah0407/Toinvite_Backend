from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import ExportImportExcel, APIGuestViewSet, APIGuestList, APIFileExample

router = routers.DefaultRouter()

router.register('api/guest', APIGuestViewSet, 'guest'),

urlpatterns = [
    path('', include(router.urls)),
    path('api/excel-export/', ExportImportExcel.as_view()),
    path('api/guest-list/', APIGuestList.as_view()),
    path('api/file_example/', APIFileExample.as_view()),
]