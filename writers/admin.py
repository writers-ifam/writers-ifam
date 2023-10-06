from django.contrib import admin
from .models import Author,Book, Poem


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Poem)