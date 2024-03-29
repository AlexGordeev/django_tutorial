from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

from .forms import ContactForm, NewsForm, UserLoginForm, UserRegisterForm
from .models import Category, News
from .utils import MyMixin


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'news/register.html', {'form': form})


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()

    return render(request, 'news/login.html', {'form': form})


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')


def send_email(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            result = send_mail(
                form.cleaned_data.get('subject'),
                form.cleaned_data.get('content'),
                settings.EMAIL_HOST_USER,
                ['metalfan665@rambler.ru'],
                fail_silently=True,
            )
            if result:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка при заполнении полей')
    else:
        form = ContactForm()

    return render(request, 'news/send_email.html', {'form': form})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2

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
    paginate_by = 2

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
