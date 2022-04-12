from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                    'phone_number', 'address', 'city')
    list_filter = ('is_staff', 'username', 'email')
    list_display_links = ('username',)
    list_editable = ('is_staff',)
