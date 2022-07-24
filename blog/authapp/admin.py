from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import BlogUserCreationForm, BlogUserChangeForm
from .models import BlogUser

class BlogUserAdmin(UserAdmin):
    add_form = BlogUserCreationForm
    form = BlogUserChangeForm
    model = BlogUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_author']
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal info', {'fields': (
            'username', 
            'email', 
            'first_name',
            'last_name',
            'password',
            'is_deleted',
        )}),
        ('Permissions', {'fields': (
            'is_admin', 
            'is_moderator',
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions',
        )}),
        ('Important dates', {'fields': (
            'last_login',
            'date_joined',
        )}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('username', 'email',)
    ordering = ('email',)

admin.site.register(BlogUser, BlogUserAdmin) #
