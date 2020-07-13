from rest_framework import serializers

from .models import Recipe

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','author','description','ingredients','created_at')
        model = Recipe
        