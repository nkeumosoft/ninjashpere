from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Post, Comment, Member


def like_post_view(request, pk):
    ...


def like_comment_view(request, pk):
    ...


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


class MemberView(View):
    template_name = ""

    def post(self, request, *args, **kwargs):
        ...

    def get(self, request, *args, **kwargs):
        ...


class PostCreateView(CreateView):
    model = Post
    template_name = ""
    fields = ["post_type", "title", "content", "key_words", "picture"]

    def post(self, request, *args, **kwargs):
        ...


class PostUpdateView(UpdateView):
    model = Post
    template_name = ""
    fields = ["post_type", "title", "content", "key_words", "picture"]

    def post(self, request, *args, **kwargs):
        ...


class CommentCreateView(CreateView):
    model = Comment
    template_name = ""
    fields = ["content"]

    def post(self, request, *args, **kwargs):
        ...


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = ""
    fields = ["content"]

    def post(self, request, *args, **kwargs):
        ...
