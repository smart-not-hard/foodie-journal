from django.urls import path
from .views import RecipesList, RecipesDetail

urlpatterns = [
    path('', RecipesList.as_view(), name='recipes_list'),
    path('<int:pk>/', RecipesDetail.as_view(), name='recipes_detail'),
]
