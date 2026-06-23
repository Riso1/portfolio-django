from django.urls import path
from .views import (
    home,
    project_detail,
    robots_txt,
    sitemap_xml,
    template_demo_list,
    template_demo_detail,
    project_order,
    project_order_success,
    legal_document,
)

urlpatterns = [
    path('', home, name='home'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
    path('templates/', template_demo_list, name='template_demo_list'),
    path('templates/<slug:slug>/', template_demo_detail, name='template_demo_detail'),
    path('order/', project_order, name='project_order'),
    path('order/success/', project_order_success, name='project_order_success'),
    path('legal/<slug:slug>/', legal_document, name='legal_document'),
]