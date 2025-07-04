from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    # Login con template personalizado y form personalizado
    path(
        "login/",
        views.LoginView.as_view(),
        name="login"
    ),

    # Logout usando método GET con redirección a home
    path(
        "logout/",
        views.LogoutView.as_view(),
        name="logout"
    ),

    # Signup
    path("signup/", views.SignUpView.as_view(), name="signup"),

    # Perfil
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit/", views.ProfileUpdateView.as_view(), name="profile_edit"),
    path("profile/edit_extended/", views.ProfileExtendedUpdateView.as_view(), name="profile_extended_edit"),

    # Cambio de contraseña
    path(
        "password_change/",
        views.ChangePasswordView.as_view(),
        name="password_change",
    ),
]
