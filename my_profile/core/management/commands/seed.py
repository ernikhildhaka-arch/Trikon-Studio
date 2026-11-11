from django.core.management.base import BaseCommand
from projects.models import Project
from team.models import TeamMember


class Command(BaseCommand):
    help = "Load the starter team and projects"

    def handle(self, *args, **options):
        team = [
            ("Aman Rana", "Founder, strategy and AI", "MBA, Data Science and AI student. Leads strategy, client communication and AI projects."),
            ("Team member 2", "Web design and development", "Builds fast, responsive websites and handles interface design."),
            ("Team member 3", "VR and 3D", "Creates immersive 3D environments and interactive prototypes."),
        ]
        for i, (n, r, b) in enumerate(team):
            TeamMember.objects.get_or_create(name=n, defaults={"role": r, "bio": b, "order": i})
        projects = [
            ("3D VR Environment", "vr", 2025, "Problem: show a university space in an interactive, explorable way.\nSolution: an immersive 3D environment with easy navigation.\nResult: selected for Phase 1 and Phase 2 of Project Expo 2025."),
            ("AI and defense technology concept", "ai", 2026, "Problem: explain a complex AI system clearly.\nSolution: a concept built around simulation and operational clarity.\nResult: presented as a future-ready application idea."),
            ("AI Fest student coordination", "strategy", 2026, "Problem: run a large university innovation event smoothly.\nSolution: coordinated teams, schedules and communication.\nResult: earned a Certificate of Appreciation."),
        ]
        for t, c, y, s in projects:
            Project.objects.get_or_create(title=t, defaults={"category": c, "year": y, "summary": s})
        self.stdout.write(self.style.SUCCESS("Seeded team and projects."))
