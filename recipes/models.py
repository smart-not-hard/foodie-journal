
from django.contrib.auth import get_user_model
from django.db import models



# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    ingredients = models.TextField()
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:16]  # [:16] new title limit from 64

