from rest_framework import serializers
from .models import *
from rest_framework_csv import renderers as r
from rest_framework.settings import api_settings
from src.events.serializers import EventsTitleSerializer


class GuestsListSerializer(serializers.ModelSerializer):
    # event = EventsTitleSerializer(read_only=True)
    event = serializers.SerializerMethodField()

    def get_event(self, instance):
        return instance.event.title

    class Meta:
        model = GuestsList
        fields = ("full_name", "phone_number", "status","event")

    def get_labels():
        return dict([(f.name, f.verbose_name) for f in GuestsList._meta.fields + GuestsList._meta.many_to_many])




class GuestsUploudSerializer(serializers.ModelSerializer):
    guests_admin = GuestsListSerializer(many=True, read_only=True)

    class Meta:
        model = GuestsAdmin
        fields = ("id", "user", "guests_admin")


class ListGuestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestsList
        fields = ("full_name", "phone_number","status")


class GuestsListItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsList
        fields = "__all__"



class GuestsListCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsList
        fields = ['status',]

