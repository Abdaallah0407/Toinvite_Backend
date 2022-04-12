from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import ExportImportExcel

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('api/excel-export/', ExportImportExcel.as_view()),
]