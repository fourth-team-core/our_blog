from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BlogUserCreationForm

class BlogUserSignUpView(CreateView):
    form_class = BlogUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
