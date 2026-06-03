from django.shortcuts import render
from .models import (
    SiteSettings,
    PageSection,
    TextBlock,
    Technology,
    HeroStat,
    ContactLink,
    Project,
    Certificate,
)


def home(request):
    site_settings = SiteSettings.objects.first()

    sections = {
        section.key: section
        for section in PageSection.objects.filter(is_published=True)
    }

    text_blocks = {
        block.key: block
        for block in TextBlock.objects.filter(is_published=True)
    }

    technologies = Technology.objects.filter(is_published=True)
    hero_stats = HeroStat.objects.filter(is_published=True)
    contact_links = ContactLink.objects.filter(is_published=True)
    projects = Project.objects.filter(is_published=True)
    certificates = Certificate.objects.filter(is_published=True)

    context = {
        'settings': site_settings,
        'sections': sections,
        'text_blocks': text_blocks,
        'technologies': technologies,
        'hero_stats': hero_stats,
        'contact_links': contact_links,
        'projects': projects,
        'certificates': certificates,
    }

    return render(request, 'portfolio/index.html', context)