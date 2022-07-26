from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import BlogUser


class BlogUserCreationForm(UserCreationForm):

    class Meta:
        model = BlogUser
        fields = ('first_name', 'last_name', 'username', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True


class BlogUserChangeForm(UserChangeForm):

    class Meta:
        model = BlogUser
        fields = ('first_name', 'last_name', 'username', 'email',)
