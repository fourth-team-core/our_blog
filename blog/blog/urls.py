from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from mainapp.views import PostsList

urlpatterns = [
    path('auth/', include('authapp.urls')),
    path('admin/', admin.site.urls),
    path('', PostsList.as_view(template_name='home.html'), name='home'),
]
