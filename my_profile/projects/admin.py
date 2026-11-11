from django.contrib import admin
from .models import Project
from core.admin import admin_site


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "year", "published")
    list_filter = ("category", "published")
    list_editable = ("published",)
    search_fields = ("title", "summary")
    list_per_page = 20


admin_site.register(Project, ProjectAdmin)
