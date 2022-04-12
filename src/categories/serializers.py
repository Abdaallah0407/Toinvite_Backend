from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"