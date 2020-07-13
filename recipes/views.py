from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView  #, APIView
# from django.views.generic.detail import DetailView


from .models import Recipe
from .serializers import RecipesSerializer
from .permissions import ISAuthorOrReadOnly

# Create your views here.
class RecipesList(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

class RecipesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (ISAuthorOrReadOnly)
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

# class RecipeCreate(ListCreateAPIView):

