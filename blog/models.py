from django.db import models
from django.urls import reverse # new

# Create your models/database/table here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,) # foreignkey for many-to-one relationship. User can be author of more post but not the opposite.
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])
