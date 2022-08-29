from django.urls import path
<<<<<<< HEAD
from mainapp.views import PostDetailView, PostCreateView, UserPostsList, PostUpdateView, PostDeleteView, search_results, PostByCategoryView
=======
from mainapp.views import PostDetailView, PostCreateView, UserPostsList, UserPostComments, PostUpdateView, PostDeleteView, search_results
>>>>>>> 18099bacf70d915ebf939317c3783ecd896cfe28

app_name = "mainapp"

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
    path("users_posts/", UserPostsList.as_view(), name="user-posts"),
    path("users_comments/", UserPostComments.as_view(), name="user-comments"),
    path("search_results/", search_results, name="search-results"),
    path("category/<int:pk>", PostByCategoryView.as_view(), name="category_posts_lst")
]