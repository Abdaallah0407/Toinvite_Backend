from django.db.models import fields
from rest_framework import serializers
from .models import BackCall

class BackCallSerializer(serializers.ModelSerializer):

    class Meta:
        model = BackCall
        fields = "__all__"

    def create(self, validated_data):
        client = BackCall.objects.create(**validated_data)

        return client