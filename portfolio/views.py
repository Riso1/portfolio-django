from django.shortcuts import render, get_object_or_404
from .models import (
    SiteSettings,
    PageSection,
    TextBlock,
    TimelineItem,
    Technology,
    HeroStat,
    ContactLink,
    Project,
    Certificate,
)
from django.http import HttpResponse
from django.urls import reverse


def home(request):
    site_settings = SiteSettings.objects.first()

    sections = {
        section.key: section
        for section in PageSection.objects.filter(is_published=True)
    }

    menu_sections = PageSection.objects.filter(
        is_published=True,
        show_in_menu=True,
    )

    text_blocks = {
        block.key: block
        for block in TextBlock.objects.filter(is_published=True)
    }

    technologies = Technology.objects.filter(is_published=True)
    hero_stats = HeroStat.objects.filter(is_published=True)
    contact_links = ContactLink.objects.filter(is_published=True)
    projects = Project.objects.filter(is_published=True)
    certificates = Certificate.objects.filter(is_published=True)

    experience_items = TimelineItem.objects.filter(
        category='experience',
        is_published=True
    )

    education_items = TimelineItem.objects.filter(
        category='education',
        is_published=True
    )

    context = {
        'settings': site_settings,
        'sections': sections,
        'text_blocks': text_blocks,
        'technologies': technologies,
        'hero_stats': hero_stats,
        'contact_links': contact_links,
        'projects': projects,
        'certificates': certificates,
        'experience_items': experience_items,
        'education_items': education_items,
        'menu_sections': menu_sections,
    }

    return render(request, 'portfolio/index.html', context)

def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
        is_published=True,
    )

    context = {
        'project': project,
        'settings': SiteSettings.objects.first(),
    }

    return render(request, 'portfolio/project_detail.html', context)

def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://m0r64n4.ru/sitemap.xml
"""
    return HttpResponse(content, content_type='text/plain')


def sitemap_xml(request):
    projects = Project.objects.filter(is_published=True, slug__isnull=False)

    urls = [
        request.build_absolute_uri(reverse('home')),
    ]

    for project in projects:
        urls.append(
            request.build_absolute_uri(
                reverse('project_detail', kwargs={'slug': project.slug})
            )
        )

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url in urls:
        xml.append('    <url>')
        xml.append(f'        <loc>{url}</loc>')
        xml.append('    </url>')

    xml.append('</urlset>')

    return HttpResponse('\n'.join(xml), content_type='application/xml')