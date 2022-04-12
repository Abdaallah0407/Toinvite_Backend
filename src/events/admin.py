from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import *



class GuestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        self.fields['numeration'].initial = len(Guests.objects.all()) + 1
        
# Register your models here.
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categories', 'get_image')
    list_filter = ('title',)
    list_display_links = ('title',)
    search_fields = ('title', 'description',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="200" height="100">')
        else:
            pass

    get_image.short_description = "Миниатюра"


@admin.register(Guests)
class GuestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','numeration',)
    ordering = ('numeration',)
    form = GuestForm