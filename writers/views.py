from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Book, Poem
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse


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
    })