from django.contrib import admin
from .models import Profile
from django.utils.html import format_html

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birthdate', 'avatar_preview')
    search_fields = ('user__username', 'bio')

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" style="object-fit: cover; border-radius: 50%;" />', obj.avatar.url)
        return "-"
    avatar_preview.short_description = 'Avatar'

# Registra el modelo Profile, pero solo si no está registrado previamente
try:
    admin.site.register(Profile, ProfileAdmin)
except admin.sites.AlreadyRegistered:
    pass  # Si ya está registrado, no hace nada
