from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView, PasswordChangeView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileUpdateForm
from .models import Profile  # Importa el modelo Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        messages.success(self.request, "Cuenta creada exitosamente. Ahora podés ingresar.")
        return super().form_valid(form)


class LoginView(AuthLoginView):
    template_name = "accounts/login.html"
    authentication_form = CustomAuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña incorrectos.")
        return super().form_invalid(form)


class LogoutView(AuthLogoutView):
    next_page = reverse_lazy("core:home")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name", "email"]
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self):
        return self.request.user


class ProfileExtendedUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "accounts/profile_extended_edit.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self):
        return self.request.user.profile


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/password_change_form.html"
    success_url = reverse_lazy("accounts:profile")

    def form_valid(self, form):
        messages.success(self.request, "Contraseña actualizada correctamente.")
        return super().form_valid(form)
