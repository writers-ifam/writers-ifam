from django.shortcuts import render, get_object_or_404
from .models import Author, Book


def index(request):
    return render(request, 'writers/index.html', {'page_title': 'Writers!'})


def login(request):
    return render(request, 'writers/login.html', {'page_title': 'Login!'})



def authors(request):
    authors = Author.objects.all().filter(is_published=True)
    return render(request, 'writers/authors.html', {'page_title': 'Authors!','authors': authors,})

def author_detail(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'writers/partials/author_detail.html', {'author': author,})

def books(request):
    books = Book.objects.all()
    return render(request, 'writers/books.html', {'page_title': 'Book!','books':books,})

def team(request):
    return render(request, 'writers/team.html', {'page_title': 'Team!',})


def book_detail(request, id):
    book = get_object_or_404(
        Book,
        id=id,
    )
    return render(request, 'writers/book_detail.html', 
    {'page_title': 'book_detail!',
     'book': book,
     })