from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author, Genre


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        books = Book.objects.all()
        numb = books.count
        authors = Author.objects.all().count()
        return render(request, self.template_name, {'books': books, 'numb': numb, 'authors': authors})


class AuthorsView(TemplateView):
    template_name = 'catalog/authors.html'

    def get(self, request):
        authors = Author.objects.all()
        params = {
            'authors':  authors
        }
        return render(request, self.template_name, params)


class GenresView(TemplateView):
    template_name = 'catalog/genres.html'

    def get(self, request):
        genres = Genre.objects.all()
        params = {
            'genres':  genres
        }
        return render(request, self.template_name, params)


class BookView(TemplateView):
    template_name = 'catalog/book.html'

    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, self.template_name, {'book': book})


class AuthorView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, first_name, last_name):
        author = Author.objects.get(first_name=first_name, last_name=last_name)
        books = Book.objects.filter(author=author)
        params = {
            'books': books,
            'author': author
        }
        return render(request, self.template_name, params)


class GenreView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, name):
        genre = Genre.objects.get(name=name)
        books = Book.objects.filter(genre=genre)
        params = {
            'books': books,
            'genre': genre
        }
        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = 'catalog/index.html'

    def post(self, request):
        content = request.POST['content']
        # search_author = Author.objects.get(first_name__icontains=content)
        books_by_title = Book.objects.filter(title__icontains=content)
        books_by_summary = Book.objects.filter(summary__icontains=content)
        # books_by_author = Book.objects.filter(author=search_author)
        result = books_by_title.union(books_by_summary, all=False)
        params = {
            'books': result
        }
        return render(request, self.template_name, params)
