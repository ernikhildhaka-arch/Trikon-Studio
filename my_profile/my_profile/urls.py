from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve

from core.admin import admin_site  # custom admin site

urlpatterns = [
    path("admin/", admin_site.urls),
    path("projects/", include("projects.urls")),
    path("", include("core.urls")),
    # Serve uploaded media files (images) in both development AND production
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]
