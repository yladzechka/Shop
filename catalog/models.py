from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="genres/", blank=True, default="image-placeholder.jpeg")

    def __str__(self):
        return self.name

    def get_genre_url(self):
        return reverse('catalog-genre', args=[self.name])


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="authors/", blank=True, default="photo-placeholder.png")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_author_url(self):
        return reverse('catalog-author', args=[self.first_name, self.last_name])


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1200, help_text="Enter a description of the book")
    genre = models.ManyToManyField(Genre)
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    image = models.ImageField(upload_to="books/", blank=True, default="book-placeholder.jpeg")

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    def get_book_url(self):
        return reverse('catalog-book', args=[self.id])

    display_genre.short_description = "Genre"
