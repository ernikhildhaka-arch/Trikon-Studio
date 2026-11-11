from django.contrib import admin
from .models import TeamMember
from core.admin import admin_site


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
    list_editable = ("order",)
    search_fields = ("name", "role")


admin_site.register(TeamMember, TeamMemberAdmin)
