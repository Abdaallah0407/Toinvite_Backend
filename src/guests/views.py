from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  permissions
from django.conf import settings
from .models import *
from .serializers import *
import pandas as pd
import uuid
from src.accounts.models import User
from src.events.models import Events
# Create your views here.


# if __name__ == '__main__':
#     xlsx_to_csv_pd()
class ExportImportExcel(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    # def xlsx_to_csv_pd():
    #     data_xls = pd.read_excel('train.xlsx', index_col=0)
    #     data_xls.to_csv('2.csv', encoding='utf-8')

    def get(self, request):
        guests = GuestsList.objects.all()
        serializer = GuestsListSerializer(guests, many=True)
        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_excel(r"C:\Users\user\Downloads\Event.xlsx", encoding="UTF-8", index=False)
        return Response({'status': 200})

    # def post(self, request):
    #     admin_id, created = User.objects.get_or_create(user=request.user)
    #     exceled_uploud = ExcelFileUploud.objects.create(excel_file_uploud = request.FILES['files'])
    #     df = pd.read_excel(f"{settings.BASE_DIR}/media/{exceled_uploud.excel_file_uploud}")
    #     for guest in (df.values.tolist()):
    #         GuestsList.objects.create(admin=admin_id)
    #         print(guest)
    #     return Response({'status': 200})