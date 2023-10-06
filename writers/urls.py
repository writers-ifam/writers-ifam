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
    path("poems/", views.poems, name="poems"),
    path("poems/<int:id>/", views.poem_detail,name="poem_detail"),
    path("poems_save/<int:id>/", views.save_poems,name="save_poems"),
    path("poems_unsave/<int:id>/", views.unsave_poems,name="unsave_poems"),
    path("poems_saved/", views.poems_saved, name="poems_saved"),
]
