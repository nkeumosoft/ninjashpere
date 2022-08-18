from blog.basemanager import MemberManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Member(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(_("email adresse"), unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
    object = MemberManager()

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    picture = models.ImageField(upload_to="media/title_post")
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(auto_now=True)
    last_edit = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField()
    publish = models.BooleanField(default=True)


class Comment(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_comment = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
    likes = models.PositiveIntegerField()
