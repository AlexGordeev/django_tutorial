from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Category, News


def index(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Новости',
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def get_category(request: HttpRequest, category_id: int) -> HttpResponse:
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
        'categories': categories
    }
    return render(request, 'news/category.html', context)
