from django.urls import path
from mainapp.views import PostDetailView, PostCreateView

app_name = "mainapp"

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create")
]