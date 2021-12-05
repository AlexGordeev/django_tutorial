from django.urls import path

from .views import CreateNewsItem, HomeNews, NewsByCategory, NewsItem, register, user_login


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', NewsItem.as_view(), name='news_item'),
    path('news/add-news/', CreateNewsItem.as_view(), name='create_news_item'),
]
