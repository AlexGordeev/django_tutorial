from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, world!')


def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Тестовая страница</h1>')
