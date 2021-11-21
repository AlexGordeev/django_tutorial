from django import template
from django.db.models import Count

from news.models import Category


register = template.Library()


@register.simple_tag()
def get_categories() -> list:
    return Category.objects.all()


@register.inclusion_tag('news/categories.html')
def show_categories() -> dict:
    return {'categories': Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)}
