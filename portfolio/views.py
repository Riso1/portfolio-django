from django.shortcuts import render
from .models import SiteSettings, Project, Certificate


def home(request):
    settings = SiteSettings.objects.first()

    projects = Project.objects.filter(
        is_published=True
    )

    certificates = Certificate.objects.filter(
        is_published=True
    )

    context = {
        'settings': settings,
        'projects': projects,
        'certificates': certificates,
    }

    return render(
        request,
        'portfolio/index.html',
        context
    )
