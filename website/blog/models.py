from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    ForeignKey,
    ImageField,
    PositiveIntegerField,
    TextField,
    UUIDField,
)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from website.blog.basemanager import MemberManager


class Member(AbstractBaseUser, PermissionsMixin):
    uuid: UUIDField = models.UUIDField(primary_key=True, editable=False)
    name: CharField = models.CharField(max_length=255)
    email: EmailField = models.EmailField(_("email adresse"), unique=True)
    password: CharField = models.CharField(max_length=255)
    is_staff: BooleanField = models.BooleanField(default=False)
    is_active: BooleanField = models.BooleanField(default=True)
    date_joined: DateTimeField = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
    object = MemberManager()

    def __str__(self):
        return str(self.email)


class Post(models.Model):
    uuid: UUIDField = models.UUIDField(primary_key=True, editable=False)
    title: CharField = models.CharField(max_length=255)
    content: TextField = models.TextField()
    picture: ImageField = models.ImageField(upload_to="media/title_post")
    author: ForeignKey = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True
    )
    publish_date: DateTimeField = models.DateTimeField(auto_now=True)
    last_edit: DateTimeField = models.DateTimeField(auto_now=True)
    likes: PositiveIntegerField = models.PositiveIntegerField()
    publish: BooleanField = models.BooleanField(default=True)


class Comment(models.Model):
    uuid: UUIDField = models.UUIDField(primary_key=True, editable=False)
    author: ForeignKey = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, blank=True
    )
    post: ForeignKey = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_comment: DateTimeField = models.DateTimeField(auto_now_add=True)
    content: CharField = models.CharField(max_length=255)
    likes: PositiveIntegerField = models.PositiveIntegerField()
