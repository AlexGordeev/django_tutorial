from django.urls import path

from .views import get_category, index


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
]
