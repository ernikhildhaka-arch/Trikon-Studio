from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=80)
    bio = models.TextField()
    linkedin = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    @property
    def initials(self):
        return "".join(w[0] for w in self.name.split()[:2]).upper()

    def __str__(self):
        return self.name
