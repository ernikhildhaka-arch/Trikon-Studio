from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from core.admin import admin_site  # custom admin site

urlpatterns = [
    path("admin/", admin_site.urls),
    path("projects/", include("projects.urls")),
    path("", include("core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
