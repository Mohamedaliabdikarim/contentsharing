from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    PREDEFINED_CATEGORIES = [
        ('Ideas', 'Ideas'),
        ('Stories', 'Stories'),
        ('Articles', 'Articles'),
        ('Tutorials', 'Tutorials'),
        ('Journalism', 'Journalism'),
    ]
    
    name = models.CharField(max_length=100, choices=PREDEFINED_CATEGORIES, unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='contents')
    image = models.ImageField(upload_to='images/', default='../default_profile_tdu7ix', null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.id} {self.title}'
