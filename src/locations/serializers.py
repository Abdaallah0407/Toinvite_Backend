from rest_framework import serializers

from src.locations.models import Address, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityUpdateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    city_title = serializers.SerializerMethodField()

    def get_city_title(sefl, instance):
        try:
            return instance.city.name
        except:
            return ''

    class Meta:
        model = Address
        fields = '__all__'


class AddressShortSerializer(serializers.ModelSerializer):

    def get_city_title(sefl, instance):
        try:
            return instance.city.name
        except:
            return ''

    class Meta:
        model = Address
        exclude = ('latitude', 'longitude', 'numeration')


class AddressUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
