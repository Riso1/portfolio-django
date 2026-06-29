from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

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
    ProjectOrder,
    OrderProjectType,
    OrderOptionGroup,
    OrderOption,
    OrderDeadline,
    OrderWorkTerm,
    OrderWebsiteGroup,
    OrderBotGroup,
    OrderWebAppGroup,
    OrderImprovementGroup,
    OrderPaymentSettings,
    LegalDocument,
    PaymentConfirmation,
    ClientDocument,
)


try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(TextBlock)
class TextBlockAdmin(ModelAdmin):
    list_display = ('title', 'key', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'key', 'content')


@admin.register(TimelineItem)
class TimelineItemAdmin(ModelAdmin):
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
class PageSectionAdmin(ModelAdmin):
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
class TechnologyAdmin(ModelAdmin):
    list_display = ('title', 'icon_class', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title',)


@admin.register(HeroStat)
class HeroStatAdmin(ModelAdmin):
    list_display = ('value', 'label', 'is_published', 'order')
    list_editable = ('is_published', 'order')


@admin.register(ContactLink)
class ContactLinkAdmin(ModelAdmin):
    list_display = ('title', 'url', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'url')


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ('full_name', 'position', 'email', 'pwa_icon_preview')
    readonly_fields = ('pwa_icon_preview',)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def pwa_icon_preview(self, obj):
        if not obj or not obj.pwa_icon:
            return 'Не загружена'

        return format_html(
            '<img src="{}" style="width:96px;height:96px;object-fit:cover;border-radius:24px;">',
            obj.pwa_icon.url,
        )

    pwa_icon_preview.short_description = 'PWA-иконка'


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
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
class CertificateAdmin(ModelAdmin):
    list_display = ('title', 'organization', 'issue_date', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'organization')


@admin.register(TemplateUseCase)
class TemplateUseCaseAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(TemplateDemo)
class TemplateDemoAdmin(ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'is_published', 'order')
    filter_horizontal = ('use_cases',)
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published', 'order')


@admin.register(ProjectOrder)
class ProjectOrderAdmin(ModelAdmin):
    list_display = ('name', 'project_type', 'budget', 'status', 'created_at')
    list_filter = ('project_type', 'status', 'created_at')
    search_fields = ('name', 'contact', 'description')
    readonly_fields = ('created_at',)


class OrderOptionInline(TabularInline):
    model = OrderOption
    extra = 1


class OrderOptionGroupInline(TabularInline):
    model = OrderOptionGroup
    extra = 1


class BaseOrderGroupAdmin(ModelAdmin):
    list_display = ('title', 'input_type', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    inlines = [OrderOptionInline]

    project_type_slug = None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(project_type__slug=self.project_type_slug)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'project_type':
            kwargs['queryset'] = OrderProjectType.objects.filter(slug=self.project_type_slug)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.project_type_id:
            obj.project_type = OrderProjectType.objects.get(slug=self.project_type_slug)
        super().save_model(request, obj, form, change)


@admin.register(OrderWebsiteGroup)
class OrderWebsiteGroupAdmin(BaseOrderGroupAdmin):
    project_type_slug = 'website'


@admin.register(OrderBotGroup)
class OrderBotGroupAdmin(BaseOrderGroupAdmin):
    project_type_slug = 'bot'


@admin.register(OrderWebAppGroup)
class OrderWebAppGroupAdmin(BaseOrderGroupAdmin):
    project_type_slug = 'webapp'


@admin.register(OrderImprovementGroup)
class OrderImprovementGroupAdmin(BaseOrderGroupAdmin):
    project_type_slug = 'improvement'


@admin.register(OrderPaymentSettings)
class OrderPaymentSettingsAdmin(ModelAdmin):
    list_display = ('title', 'bank_name', 'recipient_name')


@admin.register(OrderProjectType)
class OrderProjectTypeAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'base_price', 'is_active', 'order')
    list_editable = ('base_price', 'is_active', 'order')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [OrderOptionGroupInline]


@admin.register(OrderDeadline)
class OrderDeadlineAdmin(ModelAdmin):
    list_display = ('title', 'multiplier', 'is_active', 'order')
    list_editable = ('multiplier', 'is_active', 'order')


@admin.register(OrderWorkTerm)
class OrderWorkTermAdmin(ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_editable = ('is_active', 'order')


@admin.register(LegalDocument)
class LegalDocumentAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'updated_at')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')


@admin.register(PaymentConfirmation)
class PaymentConfirmationAdmin(ModelAdmin):
    list_display = ('name', 'contact', 'amount', 'created_at')
    search_fields = ('name', 'contact', 'comment')
    readonly_fields = ('created_at',)

    
@admin.register(ClientDocument)
class ClientDocumentAdmin(ModelAdmin):
    list_display = ('title', 'is_published', 'order', 'created_at')
    list_editable = ('is_published', 'order')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
