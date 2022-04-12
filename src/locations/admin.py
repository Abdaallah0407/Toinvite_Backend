from django.contrib import admin
from django import forms

from src.locations.models import Address, City


class CityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['numeration'].initial = len(City.objects.all()) + 1


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'numeration')
    search_fields = ('name',)
    ordering = ('numeration',)
    form = CityForm


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['numeration'].initial = len(Address.objects.all()) + 1


class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'numeration')
    search_fields = ('name',)
    ordering = ('numeration',)
    form = AddressForm


admin.site.register(Address, AddressAdmin)
admin.site.register(City, CityAdmin)
