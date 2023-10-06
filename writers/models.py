from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='author/cover/%Y/%m/%d/', blank=True, default="")
    is_published = models.BooleanField(default=True)
    bio = models.CharField(max_length=200)
    death = models.CharField(max_length=200)
    date_birth = models.DateField(blank=False)
    date_death = models.DateField(blank=True, default=None)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.PositiveIntegerField(default=0)
    synopsis = models.TextField(default='')
    download = models.URLField()
    image = models.ImageField(upload_to='books/cover/%Y/%m/%d/', blank=True, default="")
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
class Poem(models.Model):
    title = models.CharField(max_length=100)
    mini_description = models.TextField(max_length=255)
    text = models.TextField(max_length=4000)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='saved_poems', blank=True)
    saved = models.BooleanField(default=False)


    def save(self, user):
        if user not in self.users.all():
            self.users.add(user)
            self.saved = True 
            
        else:
            self.users.remove(user)
            self.saved = False
        super().save()
        
    def unsave(self, user):
        self.users.remove(user)
        self.saved = False
        super().save()
    

    def __str__(self):
        return self.title