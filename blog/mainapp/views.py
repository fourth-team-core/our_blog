from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.models import Post


class PostsList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-published_at')


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
