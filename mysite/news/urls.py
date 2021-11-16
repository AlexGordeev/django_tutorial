from django.urls import path

from .views import add_news, get_news_item, HomeNews, NewsByCategory


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', get_news_item, name='news_item'),
    path('news/add-news/', add_news, name='add_news'),
]
