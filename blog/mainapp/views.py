from django.views.generic import ListView, DetailView, CreateView

from mainapp.models import Post


class PostsList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-published_at')


class PostDetailView(DetailView):
    model = Post
    template_name = "mainapp/post_detail.html"
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "category", "url", "content", "tags", "status", "published_at"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
