import profile
from django.shortcuts import render, get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, viewsets, parsers
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
from twilio.rest import Client
# Create your views here.
from .sms_send import sms_send


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

class APIGuestsListItemsView(viewsets.ModelViewSet):
    queryset = GuestsList.objects.all()
    serializer_class = GuestsListItemsSerializer

    # def get_queryset(self):
        
    #     queryset = GuestsList.objects.order_by('title')

    #     return queryset


class ExportImportExcel(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user = self.request.user
        # event = Events.objects.get(pk=request.data['event'])
        event = Events.objects.get(pk=request.data['event'])
        guests = GuestsList.objects.filter(admin__user=user, event=event)
        serializer = GuestsListSerializer(guests, many=True)
        df = pd.DataFrame(serializer.data)
        df.rename(columns={'full_name': 'ФИО', 'phone_number': 'Номер Телефона', 'status': 'Статус',
                  'event': 'Мероприятие'}, inplace=True)
        print(df)
        file_name = uuid.uuid4()
        df.to_excel(f"media/excel/{file_name}.xlsx",
                    encoding="UTF-8", index=False,)
        print(request.META['HTTP_HOST'])
        file_path = f"{request.META['HTTP_HOST']}/media/excel/{file_name}.xlsx"
        return Response(file_path, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UploadFileSerializer, parser_classes=(parsers.MultiPartParser, parsers.JSONParser))
    def post(self, request):
        exceled_uploud = ExcelFileUploud.objects.create(
            excel_file_uploud=request.FILES['file'])
        df = pd.read_excel(
            f"{settings.BASE_DIR}/media/{exceled_uploud.excel_file_uploud}"
        )
        for student in (df.values.tolist()):
            guest = GuestsList.objects.create(
                full_name=student[0],
                phone_number=student[1] if len(student) > 1 else None,
                admin=GuestsAdmin.objects.get(user=request.user),
                event=Events.objects.get(pk=request.data['event'])
            )
            if guest.phone_number:
                url = f"http://164.92.245.139/invitation/?guest_id={guest.id}"
                text = f'Вы были приглашены на мероприятие: {guest.event.title}. ' \
                       f'Принять или отклонить приглашение вы можете по ссылке: {url}'
                phone_number = str(guest.phone_number)
                if not phone_number[0] == '+':
                    phone_number = '+' + phone_number
                sms_send(phone_number, text)
        return Response('Import Succeeded', status=status.HTTP_200_OK)


class APIGuestList(ListAPIView):
    serializer_class = ListGuestsSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        event = Events.objects.get(pk=self.request.data['event'])

        if event.admin != self.request.user:
            return Response('You are not admin of the event', status=status.HTTP_403_FORBIDDEN)


        queryset = GuestsList.objects.filter(admin__user=user, event=event)
        return queryset



class APIFileExample(APIView):
    def get(self, request):
        file_path = f"{request.META['HTTP_HOST']}/media/import/Import_Example.xlsx"
        return Response(file_path, status=status.HTTP_200_OK)


class APIRAssylka(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, *args, **kwargs):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        user = self.request.user
        event = Events.objects.get(pk=self.request.data['event'])
        if event.admin != self.request.user:
            return Response('You are not admin of the event', status=status.HTTP_403_FORBIDDEN)

        guests = GuestsList.objects.filter(event=event)

        for guest in guests:
            if guest.phone_number:
                phone_number = "+" + guest.phone_number

                message = client.messages.create(
                    body=f'{guest.full_name}  Вы были приглашены на {guest.event} !!! Которая состоится 15 декабря в 11.00 ресторан Ала-Тоо.',
                    from_='+19592511918',
                    to=phone_number)
                print(message.sid)

            # super().save(*args, **kwargs)
        return Response('Messages sent successfully', status=status.HTTP_200_OK)




class APIInterview(UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = GuestsListCreateUpdateSerializer
    queryset = GuestsList.objects.all()

    def update(self, request, *args, **kwargs): 
        get_id = self.request.query_params.get('get_id')
        guest_item = GuestsList.objects.get(id=get_id)

        return guest_item

class APIGuestInvitation(RetrieveAPIView, UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = GuestsListSerializer
    queryset = GuestsList.objects.all()

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = InvitationSerializer(obj)
        return Response(serializer.data)