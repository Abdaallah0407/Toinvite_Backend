from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *
from src.accounts.serializers import UserDetailSerializer
from ..guests.models import GuestsList


class GuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsList
        fields = ('full_name', 'phone_number', 'status')


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"

class EventsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['title']


class EventsDetailSerializer(serializers.ModelSerializer):
    guests_list = serializers.SerializerMethodField()
    accepted = serializers.SerializerMethodField()
    declined = serializers.SerializerMethodField()
    undecided = serializers.SerializerMethodField()
    categories = serializers.SlugRelatedField(
        slug_field="title", read_only=True)
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Events
        fields = "__all__"

    def get_guests_list(self, obj):
        data = GuestListSerializer(obj.guestslist_set.all().order_by('full_name'), many=True).data
        return data

    def get_accepted(self, obj):
        return obj.guestslist_set.filter(status=True).count()

    def get_declined(self, obj):
        return obj.guestslist_set.filter(status=False).count()

    def get_undecided(self, obj):
        return obj.guestslist_set.filter(status=None).count()


class AdUnpublishedSerializer(serializers.ModelSerializer):
    admin = UserDetailSerializer()

    class Meta:
        model = Events
        fields = ['id', 'title', 'location', 'updatedAt', 'image', 'admin', ]


class AdSerializer(serializers.ModelSerializer):
    admin = UserDetailSerializer()

    class Meta:
        model = Events
        fields = ['id', 'title', 'location',
                  'updatedAt', 'image', 'admin', ]
