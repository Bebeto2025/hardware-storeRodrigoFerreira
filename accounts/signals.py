from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Intenta obtener el perfil, si no existe, lo crea
        Profile.objects.get_or_create(user=instance)
    else:
        # Solo guarda el perfil si ya existe para evitar errores
        if hasattr(instance, 'profile'):
            instance.profile.save()
