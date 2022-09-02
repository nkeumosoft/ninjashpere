from blog.models import Member
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ("email",)
