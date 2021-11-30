from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from .forms import NewsForm
from .models import Category, News
from .utils import MyMixin


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['has_link'] = True
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs.get('category_id'))
        return context

    def get_queryset(self):
        return News.objects\
            .filter(category_id=self.kwargs.get('category_id'), is_published=True)\
            .select_related('category')


class NewsItem(DetailView):
    model = News
    template_name = 'news/news_item_detail.html'
    context_object_name = 'news_item'


class CreateNewsItem(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/create_news_item.html'
    raise_exception = True
