from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('auth/', include('authapp.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('', TemplateView.as_view(template_name='mainapp/index.html'), name='index_url'),
    # path('login/', TemplateView.as_view(template_name='authapp/login1.html'), name='login_url'),
]
