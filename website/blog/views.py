from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = ""
    context_object_name = "posts"
    ordering = ["-updated_at"]
    paginate_by = 20

    def get_context_data(self, **kwargs):
        ...


class PostDetailView(DetailView):
    model = Post
    template_name = ""
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        ...
