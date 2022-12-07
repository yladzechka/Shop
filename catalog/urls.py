from django.contrib import admin
from django.urls import path, include
from .views import IndexView, BookView

# '' - домашняя страница
# 'books/' - список всех книг
# 'authors/' - список всех авторов
# 'book/<id>' - детальная информация для определенной книги
# 'author/<id>' - детальная информация для автора
urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('catalog/book-<int:id>/', BookView.as_view(), name='catalog-book')
]
