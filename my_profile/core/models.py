from django.db import models
from django.utils import timezone


class Inquiry(models.Model):
    SERVICES = [("ai", "AI, data and automation"), ("web", "Web design and development"),
                ("vr", "VR, 3D and immersive"), ("strategy", "Business strategy"),
                ("unsure", "Not sure yet")]
    BUDGETS = [("u15", "Under \u20b915,000"), ("15_45", "\u20b915,000 to \u20b945,000"),
               ("45p", "\u20b945,000 and above"), ("unsure", "Not sure yet")]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=20, choices=SERVICES)
    budget = models.CharField(max_length=20, choices=BUDGETS)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "inquiries"

    def __str__(self):
        return f"{self.name} ({self.get_service_display()})"


class PageView(models.Model):
    """Records every public page hit for the analytics dashboard."""
    DEVICE_CHOICES = [("desktop", "Desktop"), ("mobile", "Mobile"), ("tablet", "Tablet")]

    path = models.CharField(max_length=255, db_index=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    referrer = models.CharField(max_length=500, blank=True)
    device = models.CharField(max_length=10, choices=DEVICE_CHOICES, default="desktop")
    ip_hash = models.CharField(max_length=64, blank=True)  # hashed — no raw IPs stored

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "page view"
        verbose_name_plural = "page views"

    def __str__(self):
        return f"{self.path} — {self.timestamp:%Y-%m-%d %H:%M}"
