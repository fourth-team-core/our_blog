from django.urls import path
from mainapp.views import PostDetailView, PostCreateView, UserPostsList, PostUpdateView, PostDeleteView

app_name = "mainapp"

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
    path("users_posts/", UserPostsList.as_view(), name="user-posts")
]