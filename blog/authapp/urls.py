from django.urls import path, reverse_lazy
from .views import (
    BlogUserSignUpView,
    BlogUserLoginView,
    BaseUserProfileView,
    BaseUserPasswordChangeView,
    BaseUserPasswordResetView,
    )
from django.contrib.auth import views as auth_views

app_name = 'authapp'

urlpatterns = [
    path('signup/', BlogUserSignUpView.as_view(), name='signup'),
    path('login/', BlogUserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', BaseUserProfileView.as_view(), name='profile'),
    path('password_change/', BaseUserPasswordChangeView.as_view(), name='password-change'),
    path('password_reset/', BaseUserPasswordResetView.as_view(), name='password-reset'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('authapp:password-reset-complete'), 
        template_name='authapp/password_reset_confirm.html'), 
        name='password-reset-confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), 
        name='password-reset-complete'),
]