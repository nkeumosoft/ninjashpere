from blog.forms.member_forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
)
from blog.models import Comment, Member, Post
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Member
    list_display = (
        "email",
        "is_staff",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Member, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
