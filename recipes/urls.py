from django.urls import path

from .views import RecipesList, RecipesDetail, BreakfastApiView, LunchApiView, DinnerApiView, RecipeCreate
# from users.views import SignUpView

urlpatterns = [
    path('recipes/', RecipesList.as_view(),),               # home
    path('recipes/<int:pk>/', RecipesDetail.as_view(),),          # detail
    path('recipes/breakfast/',BreakfastApiView.as_view()),
    path('recipes/lunch/',LunchApiView.as_view()),
    path('recipes/dinner/',DinnerApiView.as_view()),
    path('recipes/create/', RecipeCreate.as_view()), 
]
