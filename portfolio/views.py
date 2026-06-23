from django.shortcuts import render, get_object_or_404, redirect
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
    TemplateUseCase,
    TemplateDemo,
    OrderProjectType,
    OrderDeadline,
    OrderWorkTerm,
    OrderPaymentSettings,
    LegalDocument,
)
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail


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


def template_demo_list(request):
    template_demos = TemplateDemo.objects.filter(
        is_published=True
    )
    use_cases = TemplateUseCase.objects.filter(
        is_active=True,
        templates__is_published=True,
    ).distinct()

    context = {
        'settings': SiteSettings.objects.first(),
        'template_demos': template_demos,
        'use_cases': use_cases,
        'menu_sections': PageSection.objects.filter(show_in_menu=True, is_published=True).order_by('order'),
        'text_blocks': {
            block.key: block for block in TextBlock.objects.all()
        },
        'contact_links': ContactLink.objects.filter(is_published=True).order_by('order'),
    }

    return render(request, 'portfolio/template_demo_list.html', context)


def template_demo_detail(request, slug):
    template_demo = get_object_or_404(
        TemplateDemo,
        slug=slug,
        is_published=True,
    )

    context = {
        'settings': SiteSettings.objects.first(),
        'template_demo': template_demo,
        'menu_sections': PageSection.objects.filter(show_in_menu=True, is_published=True).order_by('order'),
        'text_blocks': {
            block.key: block for block in TextBlock.objects.all()
        },
        'contact_links': ContactLink.objects.filter(is_published=True).order_by('order'),
    }

    return render(request, 'portfolio/template_demo_detail.html', context)


def project_order(request):
    site_settings = SiteSettings.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        contact = request.POST.get('contact', '').strip()
        project_type = request.POST.get('project_type', '').strip()
        budget = int(request.POST.get('budget', 0) or 0)
        description = request.POST.get('description', '').strip()
        selected_options = request.POST.get('selected_options', '').strip()

        order = ProjectOrder.objects.create(
            name=name,
            contact=contact,
            project_type=project_type,
            budget=budget,
            description=description,
            selected_options=selected_options,
        )

        subject = f'Новая заявка на проект: {order.get_project_type_display()}'
        message = (
            f'Имя: {order.name}\n'
            f'Контакт: {order.contact}\n'
            f'Тип проекта: {order.get_project_type_display()}\n'
            f'Бюджет: {order.budget} ₽\n\n'
            f'Опции:\n{order.selected_options}\n\n'
            f'Описание:\n{order.description}'
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ORDER_EMAIL_TO],
            fail_silently=True,
        )

        return redirect('project_order_success')

    project_types = (
        OrderProjectType.objects
        .filter(is_active=True)
        .prefetch_related('option_groups__options')
        .order_by('order', 'title')
    )

    deadlines = OrderDeadline.objects.filter(is_active=True).order_by('order', 'title')
    work_terms = OrderWorkTerm.objects.filter(is_active=True).order_by('order', 'title')
    payment_settings = OrderPaymentSettings.objects.first()

    context = {
        'settings': site_settings,
        'project_types': project_types,
        'deadlines': deadlines,
        'work_terms': work_terms,
        'payment_settings': payment_settings,
        'menu_sections': PageSection.objects.filter(show_in_menu=True, is_published=True).order_by('order'),
        'text_blocks': {
            block.key: block for block in TextBlock.objects.all()
        },
        'contact_links': ContactLink.objects.filter(is_published=True).order_by('order'),
    }

    return render(request, 'portfolio/project_order.html', context)


def project_order_success(request):
    context = {
        'settings': SiteSettings.objects.first(),
    }

    return render(request, 'portfolio/project_order_success.html', context)


def legal_document(request, slug):
    document = get_object_or_404(
        LegalDocument,
        slug=slug,
        is_published=True,
    )

    context = {
        'settings': SiteSettings.objects.first(),
        'document': document,
        'menu_sections': PageSection.objects.filter(show_in_menu=True, is_published=True).order_by('order'),
        'text_blocks': {
            block.key: block for block in TextBlock.objects.all()
        },
        'contact_links': ContactLink.objects.filter(is_published=True).order_by('order'),
    }

    return render(request, 'portfolio/legal_document.html', context)
