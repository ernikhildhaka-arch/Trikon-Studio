from django.shortcuts import render
from .models import Project


def project_list(request):
    cat = request.GET.get("cat", "")
    qs = Project.objects.filter(published=True)
    if cat in dict(Project.CATEGORIES):
        qs = qs.filter(category=cat)
    else:
        cat = ""
    return render(request, "projects/list.html", {"projects": qs, "categories": Project.CATEGORIES, "active": cat})
