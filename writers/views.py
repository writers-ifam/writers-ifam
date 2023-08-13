from django.shortcuts import render
from .models import Author, Book

def index(request):
    return render(request, 'writers/index.html', {'page_title': 'Writers!'})

def authors(request):
    authors = Author.objects.all().filter(is_published=True)
    return render(request, 'writers/authors.html', {'page_title': 'Authors!','authors': authors,})

def author_detail(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'writers/partials/author_detail.html', {'author': author,})

def books(request):
    books = Book.objects.all()
    return render(request, 'writers/books.html', {'page_title': 'Book!','books':books,})