from django.urls import path
from .views import BlogUserSignUpView

urlpatterns = [
    path('signup/', BlogUserSignUpView.as_view(), name='signup'),
]