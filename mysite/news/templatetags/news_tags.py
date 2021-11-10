from django import template

from news.models import Category


register = template.Library()


@register.simple_tag()
def get_categories() -> list:
    return Category.objects.all()


@register.inclusion_tag('news/categories.html')
def show_categories():
    return {'categories': Category.objects.all()}
