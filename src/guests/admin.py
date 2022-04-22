from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django import forms
from .models import *

# class GuestsListForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(GuestsListForm, self).__init__(*args, **kwargs)
#         self.fields['numeration'].initial = len(GuestsList.objects.all()) + 1

class GuestsListResource(resources.ModelResource):

    class Meta:
        model = GuestsList

@admin.register(GuestsList)
class GuestsListAdmin(ImportExportModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'admin', 'event')
    list_display_links = ('full_name',)
    list_filter = ('full_name',)
    resource_class = GuestsListResource
    # form = GuestsListForm


@admin.register(GuestsAdmin)
class GuestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',
                    'data_added')
    list_filter = ('user',)
    list_display_links = ('user',)
    search_fields = ('user', 'id')



@admin.register(ExcelFileUploud)
class ExcelFileUploudAdmin(admin.ModelAdmin):
    list_display = ('id', )