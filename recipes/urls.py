from django.urls import path

from .views import RecipesList, RecipesDetail, BreakfastApiView, LunchApiView, DinnerApiView
# from users.views import SignUpView

urlpatterns = [
    path('recipes/', RecipesList.as_view(), name='recipes_list'),               # home
    path('recipes/<int:pk>/', RecipesDetail.as_view(), name='recipes_detail'),          # detail
    path('recipes/breakfast/',BreakfastApiView.as_view()),
    path('recipes/lunch/',LunchApiView.as_view()),
    path('recipes/dinner/',DinnerApiView.as_view()),
]
