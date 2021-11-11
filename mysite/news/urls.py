from django.urls import path

from .views import get_category, get_news_item, index


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', get_news_item, name='news_item'),
]
