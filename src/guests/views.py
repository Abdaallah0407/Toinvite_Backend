from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *
from django.conf import settings
from .models import *
from .serializers import *
import pandas as pd
import numpy as np
import uuid
from src.accounts.models import User
from src.events.models import Events
from rest_framework import status
from toinvite_core.settings import BASE_DIR
# Create your views here.


class APIGuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestsUploudSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = GuestsAdmin.objects.all()

    def retrieve(self, request, pk=None):
        queryset = GuestsAdmin.objects.filter(user=pk)
        if not queryset:
            return Response([])
        locker = get_object_or_404(queryset, user=pk)
        serializer = GuestsUploudSerializer(
            locker, context={'request': request})
        return Response(serializer.data)


class ExportImportExcel(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user = self.request.user
        event = Events.objects.get(pk=request.data['event'])
        guests = GuestsList.objects.filter(admin__user=user, event=event)
        serializer = GuestsListSerializer(guests, many=True)
        df = pd.DataFrame(serializer.data)
        df.rename(columns={'full_name': 'ФИО', 'phone_number': 'Номер Телефона',
                  'event': 'Мероприятие'}, inplace=True)
        print(df)
        file_name = uuid.uuid4()
        df.to_excel(f"media/excel/{file_name}.xlsx",
                    encoding="UTF-8", index=False,)
        print(request.META['HTTP_HOST'])
        file_path = f"{request.META['HTTP_HOST']}/media/excel/{file_name}.xlsx"
        return Response(file_path, status=status.HTTP_200_OK)

    def post(self, request):
        exceled_uploud = ExcelFileUploud.objects.create(
            excel_file_uploud=request.FILES['files'])
        df = pd.read_excel(
            f"{settings.BASE_DIR}/media/{exceled_uploud.excel_file_uploud}")
        for student in (df.values.tolist()):
            GuestsList.objects.create(
                full_name=student[0],
                phone_number=student[1],
                admin=GuestsAdmin.objects.get(user=request.user),
                event=Events.objects.get(pk=request.data['event'])
            )
            print(student)
        return Response({'status': 200})


class APIGuestList(ListAPIView):
    serializer_class = ListGuestsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        event = Events.objects.get(pk=self.request.data['event'])
        queryset = GuestsList.objects.filter(admin__user=user, event=event)

        return queryset


class APIFileExample(APIView):
    def get(self, request):
        file_path = f"{request.META['HTTP_HOST']}/media/import/Import_Example.xlsx"
        return Response(file_path, status=status.HTTP_200_OK)
