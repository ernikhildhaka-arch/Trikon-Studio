from django.core.validators import FileExtensionValidator
from django.db import models


class Project(models.Model):
    CATEGORIES = [("vr", "VR and 3D"), ("ai", "AI and data"), ("web", "Web"), ("strategy", "Strategy and events")]

    title = models.CharField(max_length=120)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    year = models.PositiveIntegerField()
    summary = models.TextField(help_text="Tip: use one line each for Problem, Solution and Result.")
    video = models.FileField(
        upload_to="projects/videos/",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["mp4", "webm", "mov", "avi", "mkv", "ogg"])],
        help_text="Upload a video file for this project (MP4, WebM, MOV, etc.)",
    )
    link = models.URLField(blank=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-year", "-id"]

    def __str__(self):
        return self.title
