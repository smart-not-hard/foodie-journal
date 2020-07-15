from rest_framework import serializers

from .models import Recipe

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','author','description','ingredients', 'steps', 'meal_type', 'img_src_1', 'img_src_2', 'img_src_3', 'difficulty', 'created_at', 'updated_at')
        model = Recipe
        