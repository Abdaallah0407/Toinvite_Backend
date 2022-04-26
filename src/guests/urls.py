from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import ExportImportExcel, APIGuestViewSet, APIGuestList, APIFileExample, APIGuestsListItemsView, APIRAssylka

router = routers.DefaultRouter()

router.register('api/guest', APIGuestViewSet, 'guest'),
router.register('api/guest-edit', APIGuestsListItemsView, 'guest_list'),


urlpatterns = [
    path('', include(router.urls)),
    path('api/excel-export/', ExportImportExcel.as_view()),
    path('api/guest-list/', APIGuestList.as_view()),
    path('api/file_example/', APIFileExample.as_view()),
    path('api/rassylka/', APIRAssylka.as_view()),
]
