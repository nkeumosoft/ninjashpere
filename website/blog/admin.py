from django.contrib import admin

from blog.models import Member, Post, Comment, KeyWord


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "published_at", "updated_at")
    list_filter = ("author", "published_at", "updated_at", "post_type")
    search_fields = ("author", "title", "content")
    filter_horizontal = ("likes",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "published_at", "updated_at")
    list_filter = ("author", "post", "published_at", "updated_at")
    search_fields = ("author", "content")
    filter_horizontal = ("likes",)


admin.site.register(Member)
admin.site.register(KeyWord)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
