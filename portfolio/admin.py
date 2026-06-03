from django.contrib import admin
from .models import SiteSettings, Project, Certificate


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'email')

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'stack', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'stack')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'issue_date', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'organization')
