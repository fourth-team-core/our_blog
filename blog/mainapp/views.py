from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils.decorators import method_decorator


from mainapp.forms import CommentForm
from mainapp.models import Post, Comment, Tag



class PostsList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-created_at')


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


class UserPostComments(ListView):
    model = Comment
    template_name = "mainapp/users_comments_list.html"
    context_object_name = "comments"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_comments'] = Comment.objects.filter(author=self.request.user).order_by('-created_at')
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "mainapp/post_detail.html"
    context_object_name = 'post'
    login_url = reverse_lazy("authapp:login")
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        post_tags = Tag.objects.filter(post_tags=kwargs['object'].pk)

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()

        context.update(
            {
                'post': post,
                'comments': comments,
                'form': form,
                'post_tags': post_tags,
            }
        )

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk']).first()
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            author = self.request.user
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                author=author,  content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return HttpResponseRedirect(reverse('mainapp:post-detail', kwargs={'pk': post.pk}))
        return self.render_to_response(context=context)


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
