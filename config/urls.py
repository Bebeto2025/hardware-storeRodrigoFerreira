from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas generales (home, about)
    path("", include("core.urls")),

    # Rutas de páginas (modelo principal)
    path("pages/", include("store.urls")),

    # Rutas de cuentas (login, signup, perfil)
    path("accounts/", include("accounts.urls")),

    # Rutas de mensajería
    path("messenger/", include("messenger.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
