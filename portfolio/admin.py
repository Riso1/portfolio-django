from django.contrib import admin
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


@admin.register(TextBlock)
class TextBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'key', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'key', 'content')


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'key', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'key')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title',)


@admin.register(HeroStat)
class HeroStatAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'is_published', 'order')
    list_editable = ('is_published', 'order')


@admin.register(ContactLink)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'url')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'email')

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'stack',
        'project_status',
        'featured',
        'is_published',
        'order',
    )
    list_editable = (
        'project_status',
        'featured',
        'is_published',
        'order',
    )
    search_fields = ('title', 'stack', 'short_description')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'issue_date', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'organization')
