from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import BlogUser


class BlogUserCreationForm(UserCreationForm):

    class Meta:
        model = BlogUser
        fields = ('first_name', 'last_name', 'username', 'email',)


class BlogUserChangeForm(UserChangeForm):

    class Meta:
        model = BlogUser
        fields = ('first_name', 'last_name', 'username', 'email',)
