from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchVector

from mainapp.models import Post, PostCategory



class PostsList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-created_at')



class PostByCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'home.html'
    paginate_by = 5

    def get_queryset(self):
        self.category = PostCategory.objects.get(pk=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category)
        return queryset





class UserPostsList(ListView):
    model = Post
    template_name = "mainapp/users_posts_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_posts_page'] = True
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "mainapp/post_detail.html"
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "category", "content", "tags"]
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "category", "content", "tags"]
    template_name_suffix = '_update_form'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("mainapp:user-posts")


def search_results(request):
    q = request.GET.get('q')

    if q:
        vector = SearchVector('title', 'content')
        query = SearchQuery(q)
        posts = Post.objects.annotate(search=vector).filter(search=query)
    else:
        posts = None

    context = {'posts': posts}
    return render(request, 'mainapp/search_results.html', context)
