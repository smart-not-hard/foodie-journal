from django.urls import path
from .views import RecipesList, RecipesDetail
from users.views import SignUpView

urlpatterns = [
    path('', RecipesList.as_view(), name='recipes_list'),                       # home
    path('Recipes/', RecipesList.as_view(), name='recipes_list'),               # recipes
    path('Recipes/<int:pk>/', RecipesDetail.as_view(), name='recipes_detail'),  # detail
    path('SignUp/', SignUpView.as_view(), name='recipes_signup'),               # signup
]
