from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewsForm
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
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/category.html', context)


def get_news_item(request: HttpRequest, news_id: int) -> HttpResponse:
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'news/news_item.html', context)


def add_news(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()

    context = {'form': form}
    return render(request, 'news/add_news.html', context)
