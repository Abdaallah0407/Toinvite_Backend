from rest_framework import serializers
from .models import *


class GuestsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsList
        fields = "__all__"