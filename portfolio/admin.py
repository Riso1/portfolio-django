from django.contrib import admin
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
)


@admin.register(TextBlock)
class TextBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'key', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'key', 'content')


@admin.register(TimelineItem)
class TimelineItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'period',
        'is_published',
        'order',
    )
    list_editable = (
        'is_published',
        'order',
    )
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'subtitle', 'description')


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'key',
        'is_published',
        'show_in_menu',
        'order',
    )
    list_editable = (
        'is_published',
        'show_in_menu',
        'order',
    )
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
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = ('title', 'stack', 'short_description')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'issue_date', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'organization')


@admin.register(TemplateUseCase)
class TemplateUseCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(TemplateDemo)
class TemplateDemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'is_published', 'order')
    filter_horizontal = ('use_cases',)
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published', 'order')
