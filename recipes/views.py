from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView  #, APIView
# from django.urls import reverse_lazy
from rest_framework import filters

from .models import Recipe
from .serializers import RecipesSerializer
from .permissions import ISAuthorOrReadOnly

# Create your views here.
class RecipesList(ListAPIView):
    search_fields = ['description', 'title', 'ingredients', 'meal_type', 'difficulty']
    filter_backends = (filters.SearchFilter,)
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

class RecipeCreate(ListCreateAPIView):
    permission_classes = (ISAuthorOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

class RecipesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (ISAuthorOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

class BreakfastApiView(ListAPIView):
    queryset = Recipe.objects.filter(meal_type='Breakfast')
    serializer_class = RecipesSerializer

class LunchApiView(ListAPIView):
    queryset = Recipe.objects.filter(meal_type='Lunch')
    serializer_class = RecipesSerializer

class DinnerApiView(ListAPIView):
    queryset = Recipe.objects.filter(meal_type='Dinner')
    serializer_class = RecipesSerializer




