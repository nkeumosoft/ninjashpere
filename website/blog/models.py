import uuid

from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.last_name


class Post(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    picture = models.ImageField(upload_to=f"posts/{author}/", blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Member, related_name="liked_posts")

    def __str__(self):
        return f"{self.author} | {self.title}"


class Comment(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Member, related_name="liked_comments")

    def __str__(self):
        return f"{self.author} | {self.post} | {self.content}"
