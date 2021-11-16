from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import NewsForm
from .models import Category, News


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['has_link'] = True
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs.get('category_id'))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs.get('category_id'), is_published=True)


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
