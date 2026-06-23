import os

from django import template
from django.contrib.staticfiles.finders import find


register = template.Library()


@register.simple_tag
def cache_bust(path):
    file_path = find(path)

    if not file_path:
        return "1"

    try:
        return int(os.path.getmtime(file_path))
    except OSError:
        return "1"


@register.filter
def split_features(value):
    if not value:
        return []

    return [item.strip() for item in value.split('•') if item.strip()]
