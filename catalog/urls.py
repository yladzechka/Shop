from django.contrib import admin
from django.urls import path, include
from .views import IndexView, BookView, AuthorsView, AuthorView

# '' - домашняя страница
# 'books/' - список всех книг
# 'authors/' - список всех авторов
# 'book/<id>' - детальная информация для определенной книги
# 'author/<id>' - детальная информация для автора
urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('authors/', AuthorsView.as_view(), name='catalog-authors'),
    path('catalog/book-<int:id>/', BookView.as_view(), name='catalog-book'),
    path('catalog/<str:first_name>-<str:last_name>/', AuthorView.as_view(), name='catalog-author'),
]
