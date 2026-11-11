from django.contrib import admin
from .models import Project
from core.admin import admin_site


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "year", "has_video", "published")
    list_filter = ("category", "published")
    list_editable = ("published",)
    search_fields = ("title", "summary")
    list_per_page = 20

    @admin.display(boolean=True, description="Video")
    def has_video(self, obj):
        return bool(obj.video)


admin_site.register(Project, ProjectAdmin)
