from django import template
from django.core.cache import cache
from django.db.models import Count, Q

from news.models import Category


register = template.Library()


@register.simple_tag()
def get_categories() -> list:
    return Category.objects.all()


@register.inclusion_tag('news/categories.html')
def show_categories() -> dict:
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects\
            .annotate(cnt=Count('news', filter=Q(news__is_published=True)))\
            .filter(cnt__gt=0)
        cache.set('categories', categories)
    return {'categories': categories}
