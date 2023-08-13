from django.urls import path
from . import views

app_name = 'writers'

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.authors, name="authors"),
    path("author_detail/<int:id>", views.author_detail, name="author_detail")
]
