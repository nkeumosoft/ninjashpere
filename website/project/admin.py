from django.contrib import admin

from .models import Project, Technology


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "link")
    list_filter = ("technologies",)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
