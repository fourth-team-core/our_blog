from django.urls import path
from mainapp.views import PostDetailView

app_name = "mainapp"

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]