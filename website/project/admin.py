from django.contrib import admin

from .models import Project, Technology


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "project_name", "project_link")
    list_filter = ("project_technologies",)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id", "tech_name")


admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
