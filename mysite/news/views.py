from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import News


def index(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Новости',
    }
    return render(request, 'news/index.html', context)
