from django.urls import path
from . import views

app_name = 'writers'

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/profile/", views.index, name="profile"),
    path("login/", views.login, name="login"),
    path("authors/", views.authors, name="authors"),
    path("author_detail/<int:id>/", views.author_detail, name="author_detail"),
    path("books/", views.books, name="books"),
    path("books/<int:id>/", views.book_detail, name="book_detail"),
    path("team/", views.team, name="team"),
     
]
