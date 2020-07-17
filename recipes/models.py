
from django.contrib.auth import get_user_model
from django.db import models



# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    ingredients = models.TextField(max_length=2500)
    steps = models.TextField(max_length=2500)
    meal_type = models.CharField(max_length=16)
    img_src_1 = models.URLField(blank=True, max_length=1000)
    img_src_2 = models.URLField(blank=True,max_length=1000)
    img_src_3 = models.URLField(blank=True,max_length=1000)
    difficulty = models.CharField(max_length=16, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:16]  # [:16] new title limit from 64

