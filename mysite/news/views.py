from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Category, News


def index(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Новости',
    }
    return render(request, 'news/index.html', context)


def get_category(request: HttpRequest, category_id: int) -> HttpResponse:
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)


def get_news_item(request: HttpRequest, news_id: int) -> HttpResponse:
    news_item = News.objects.get(pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'news/news_item.html', context)
