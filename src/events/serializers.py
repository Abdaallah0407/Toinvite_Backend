from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *
from src.accounts.serializers import UserDetailSerializer


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class EventsDetailSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        slug_field="title", read_only=True)
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Events
        fields = "__all__"


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
