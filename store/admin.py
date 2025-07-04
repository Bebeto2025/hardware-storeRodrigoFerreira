from django.contrib import admin
from .models import Page
from django.utils.html import format_html

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at', 'image_preview')
    search_fields = ('title', 'subtitle')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Imagen'
