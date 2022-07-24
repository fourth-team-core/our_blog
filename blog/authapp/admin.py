from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import BlogUserCreationForm, BlogUserChangeForm
from .models import BlogUser

class BlogUserAdmin(UserAdmin):
    add_form = BlogUserCreationForm
    form = BlogUserChangeForm
    model = BlogUser
    list_display = ['email', 'username',]

admin.site.register(BlogUser, BlogUserAdmin)
