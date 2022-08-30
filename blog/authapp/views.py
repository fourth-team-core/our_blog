from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordResetView)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import BlogUserCreationForm, EmailValidationOnForgotPassword


class BlogUserSignUpView(CreateView):
    form_class = BlogUserCreationForm
    success_url = reverse_lazy("authapp:login")
    template_name = "authapp/signup.html"


class BlogUserLoginView(LoginView):
    template_name = "authapp/login.html"


class BaseUserProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("authapp:login")
    template_name = "authapp/profile.html"


class BaseUserPasswordChangeView(
    LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView
):
    login_url = reverse_lazy("authapp:login")
    success_message = "Congrats, your password has been successfully changed!"
    success_url = reverse_lazy("authapp:login")
    template_name = "authapp/password_change.html"


class BaseUserPasswordResetView(PasswordResetView):
    form_class = EmailValidationOnForgotPassword
    success_url = reverse_lazy("authapp:login")
    template_name = "authapp/password_reset.html"
    email_template_name = "authapp/password_reset_email.html"
    subject_template_name = "authapp/password_reset_subject.txt"
