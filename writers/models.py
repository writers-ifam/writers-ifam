from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='author/cover/%Y/%m/%d/', blank=True, default="")
    bio = models.CharField(max_length=200)
    death = models.CharField(max_length=200)
    date_birth = models.DateField(blank=False)
    date_death = models.DateField(blank=True, default=None)
    
    def __str__(self):
        return self.name
    
