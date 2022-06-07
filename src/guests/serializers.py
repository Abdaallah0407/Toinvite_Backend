from rest_framework import serializers
from .models import *

class InvitationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsList
        fields = ('status',)


class InvitationSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='event.title')
    date_start = serializers.SerializerMethodField()
    date_end = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = GuestsList
        fields = ('title', 'date_start', 'date_end', 'location', 'status')

    def get_date_start(self, obj):
        return obj.event.dateAt

    def get_date_end(self, obj):
        return obj.event.dateEnd

    def get_location(self, obj):
        location = ''
        if obj.event.location:
            location += obj.event.location.name
            if obj.event.location.city:
                location += f', {obj.event.location.city.name}'
            return location
        return None


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    event = serializers.IntegerField()


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
        fields = ("id","full_name", "phone_number","status")


class GuestsListItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsList
        fields = ("full_name", "phone_number","status")



class GuestsListCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsList
        fields = ['status',]

