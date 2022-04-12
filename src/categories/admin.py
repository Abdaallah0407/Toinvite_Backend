from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image')
    list_filter = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.icon.url} width="100" height="80">')