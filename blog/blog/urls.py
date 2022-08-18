from django.contrib import admin
from django.urls import include, path
from mainapp.views import PostsList, CategoryPostsList

urlpatterns = [
    path("auth/", include("authapp.urls")),
    path("admin/", admin.site.urls),
    path("posts/", include("mainapp.urls")),
    path("", PostsList.as_view(template_name="home.html"), name="home"),
    path("", include("social_django.urls", namespace="social")),
    # path("category<slug:id>", CategoryPostsList.as_view(), name="category_posts_lst")
]
