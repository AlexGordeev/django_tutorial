from django.urls import path

from .views import add_news, get_category, get_news_item, HomeNews


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', get_news_item, name='news_item'),
    path('news/add-news/', add_news, name='add_news'),
]
