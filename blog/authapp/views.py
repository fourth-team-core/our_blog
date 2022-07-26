from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from .forms import BlogUserCreationForm


class BlogUserSignUpView(CreateView):
    form_class = BlogUserCreationForm
    success_url = reverse_lazy('authapp:login')
    template_name = 'authapp/signup.html'


class BlogUserLoginView(LoginView):
    template_name = 'authapp/login.html'


class BaseUserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'authapp/profile.html'
