from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from projects.models import Project
from team.models import TeamMember
from .forms import InquiryForm


def home(request):
    form = InquiryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        inq = form.save()
        send_mail(
            f"New inquiry from {inq.name}",
            f"Service: {inq.get_service_display()}\nBudget: {inq.get_budget_display()}\n"
            f"Email: {inq.email}\n\n{inq.message}",
            settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL], fail_silently=True,
        )
        messages.success(request, "Thanks! We have your message and will reply within 24 hours.")
        return redirect(reverse("home") + "#contact")
    return render(request, "core/home.html", {
        "form": form,
        "projects": Project.objects.filter(published=True)[:3],
        "team": TeamMember.objects.all(),
        "contact_email": settings.CONTACT_EMAIL,
    })
