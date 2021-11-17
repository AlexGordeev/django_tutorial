from django.urls import path

from .views import add_news, HomeNews, NewsByCategory, NewsItem


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', NewsItem.as_view(), name='news_item'),
    path('news/add-news/', add_news, name='add_news'),
]
