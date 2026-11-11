from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from django.utils.html import format_html

from .models import Inquiry, PageView


# ─── Inquiry Admin ────────────────────────────────────────────────────────────

class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "budget", "created", "status_badge")
    list_filter = ("service", "handled", "created")
    search_fields = ("name", "email", "message")
    list_per_page = 20
    date_hierarchy = "created"
    readonly_fields = ("created",)
    actions = ["mark_handled", "mark_pending"]

    fieldsets = (
        ("Contact Information", {
            "fields": ("name", "email")
        }),
        ("Inquiry Details", {
            "fields": ("service", "budget", "message", "created")
        }),
        ("Status", {
            "fields": ("handled",)
        }),
    )

    @admin.display(description="Status", ordering="handled")
    def status_badge(self, obj):
        if obj.handled:
            return format_html(
                '<span style="background:#10b981;color:#fff;padding:3px 10px;'
                'border-radius:12px;font-size:11px;font-weight:600;">{}</span>',
                "✓ Handled",
            )
        return format_html(
            '<span style="background:#f59e0b;color:#fff;padding:3px 10px;'
            'border-radius:12px;font-size:11px;font-weight:600;">{}</span>',
            "⏳ Pending",
        )

    @admin.action(description="Mark selected as handled")
    def mark_handled(self, request, queryset):
        updated = queryset.update(handled=True)
        self.message_user(request, f"{updated} inquiries marked as handled.")

    @admin.action(description="Mark selected as pending")
    def mark_pending(self, request, queryset):
        updated = queryset.update(handled=False)
        self.message_user(request, f"{updated} inquiries marked as pending.")


# ─── PageView Admin ───────────────────────────────────────────────────────────

class PageViewAdmin(admin.ModelAdmin):
    list_display = ("path", "device_icon", "timestamp", "referrer_short")
    list_filter = ("device", "path")
    search_fields = ("path", "referrer")
    date_hierarchy = "timestamp"
    list_per_page = 50
    readonly_fields = ("path", "timestamp", "referrer", "device", "ip_hash")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    @admin.display(description="Device")
    def device_icon(self, obj):
        icons = {"desktop": "🖥️ Desktop", "mobile": "📱 Mobile", "tablet": "📟 Tablet"}
        return icons.get(obj.device, obj.device)

    @admin.display(description="Referrer")
    def referrer_short(self, obj):
        if not obj.referrer:
            return "—"
        short = obj.referrer[:60]
        return format_html(
            '<span title="{}">{}</span>',
            obj.referrer,
            short + ("…" if len(obj.referrer) > 60 else ""),
        )


# ─── Custom Admin Site ────────────────────────────────────────────────────────

class MyProfileAdminSite(admin.AdminSite):
    site_header = "⚡ My Portfolio Admin"
    site_title = "Portfolio Admin"
    index_title = "Dashboard"

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        now = timezone.now()
        today = now.date()

        total_views = PageView.objects.count()
        today_views = PageView.objects.filter(timestamp__date=today).count()
        week_views = PageView.objects.filter(
            timestamp__date__gte=today - timezone.timedelta(days=6)
        ).count()

        top_pages = (
            PageView.objects.values("path")
            .annotate(hits=Count("id"))
            .order_by("-hits")[:5]
        )

        daily = (
            PageView.objects.filter(timestamp__date__gte=today - timezone.timedelta(days=6))
            .annotate(day=TruncDate("timestamp"))
            .values("day")
            .annotate(hits=Count("id"))
            .order_by("day")
        )
        chart_labels = []
        chart_data = []
        day_map = {row["day"]: row["hits"] for row in daily}
        for i in range(6, -1, -1):
            d = today - timezone.timedelta(days=i)
            chart_labels.append(d.strftime("%d %b"))
            chart_data.append(day_map.get(d, 0))

        device_counts = (
            PageView.objects.values("device")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        pending_inquiries = Inquiry.objects.filter(handled=False).count()
        recent_inquiries = Inquiry.objects.order_by("-created")[:5]

        extra_context.update({
            "total_views": total_views,
            "today_views": today_views,
            "week_views": week_views,
            "top_pages": list(top_pages),
            "chart_labels": chart_labels,
            "chart_data": chart_data,
            "device_counts": list(device_counts),
            "pending_inquiries": pending_inquiries,
            "recent_inquiries": recent_inquiries,
        })
        return super().index(request, extra_context)


# Instantiate the custom admin site
admin_site = MyProfileAdminSite(name="admin")

# Register auth models
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)

# Register models on our custom site
admin_site.register(Inquiry, InquiryAdmin)
admin_site.register(PageView, PageViewAdmin)
