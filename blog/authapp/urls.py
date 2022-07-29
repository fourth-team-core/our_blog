from django.urls import path, include
from .views import BlogUserSignUpView, BlogUserLoginView, BaseUserProfileView
from django.contrib.auth import views as auth_views

app_name = 'authapp'

urlpatterns = [
    path('signup/', BlogUserSignUpView.as_view(), name='signup'),
    path('login/', BlogUserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', BaseUserProfileView.as_view(), name='profile'),
]