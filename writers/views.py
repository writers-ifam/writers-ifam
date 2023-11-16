from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Book, Poem
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    return render(request, 'writers/index.html', {'page_title': 'Writers!'})


def login(request):
    return render(request, 'writers/login.html', {'page_title': 'Login!'})



def authors(request):
    page_title = 'Authors!'
    authors = Author.objects.all().filter(is_published=True, is_dead=True, is_poem_author=True)
    if request.method == "POST":
        search = request.POST.get('home-searchbar')
        if len(search) > 0:    
            authors = Author.objects.all().filter(
                Q(name__icontains=search) |
                Q(death__icontains=search) | 
                Q(bio__icontains=search), is_published=True, is_dead=True, is_poem_author=True)
    
    paginator = Paginator(authors, 15)
    page_number = request.GET.get("page")
    authors = paginator.get_page(page_number)

    return render(request, 'writers/authors.html', {'page_title': page_title,'authors': authors,})

def author_detail(request, id):
    author = Author.objects.get(id=id)
    poems_by_author = Poem.objects.filter(author=author)[:3]
    return render(request, 'writers/partials/author_detail.html', {'author': author,'poems_by_author': poems_by_author})

def books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get("page")
    books = paginator.get_page(page_number)
    return render(request, 'writers/books.html', {'page_title': 'Book!','books':books,})

def team(request):
    return render(request, 'writers/team.html', {'page_title': 'Team!',})


def book_detail(request, id):
    book = get_object_or_404(
        Book,
        id=id,
    )
    return render(request, 'writers/book_detail.html', 
    {'page_title': book.title.title() + ' - Writers',
     'book': book,
     })

def poems(request):
    last_poem = Poem.objects.last()
    poem = Poem.objects.all().exclude(id=last_poem.id)
    return render(request, 'writers/poems.html', {'page_title': 'Poems!',
     'poems': poem,
     'last_poem': last_poem,
     })
    
    
    

def poem_detail(request, id): 
    poem = get_object_or_404(
        Poem,
        id=id,
    )
    
    saved = False
    if poem.users.filter(id=request.user.id).exists():
        saved = True
    else:
        saved = False
    
    return render(request, 'writers/poem.html', 
    {'page_title': poem.title,
     'poem': poem,
     'saved': saved,
     })
    
@login_required(login_url=reverse_lazy('account_login'))
def save_poems(request, id):
    poem = get_object_or_404(Poem, id=id)
    poem.save(request.user)
    
    return redirect('writers:poems')

@login_required(login_url=reverse_lazy('account_login'))
def unsave_poems(request, id):
    poem = get_object_or_404(Poem, id=id)
    poem.unsave(request.user)
    
    return redirect('writers:poems')

@login_required(login_url=reverse_lazy('account_login'))
def poems_saved(request):
    poems = Poem.objects.filter(users=request.user)

    return render(request, 'writers/saved.html',{
        'page_title': "Favoritos",
        'poems': poems,
        'is_saved': True,
    })