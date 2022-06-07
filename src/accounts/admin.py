from django.contrib import admin
from .models import *
# Register your models here.
from ..guests.models import GuestsAdmin


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                    'phone_number', 'address', 'city')
    list_filter = ('is_staff', 'username', 'email')
    list_display_links = ('username',)
    list_editable = ('is_staff',)

    def save_model(self, request, obj, form, change):
        super(ProductAdmin, self).save_model(request, obj, form, change)
        GuestsAdmin.objects.get_or_create(user=obj)
        obj.set_password(form.cleaned_data['password'])
        obj.save()
