from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from mainapp.models import Post


class PostsList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-published_at')

