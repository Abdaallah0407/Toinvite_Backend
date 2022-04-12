# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(BackCall)
class BackCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email')
    list_filter = ('name',)
    list_display_links = ('name',)