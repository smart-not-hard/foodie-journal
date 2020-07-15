from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from django.contrib.auth.models import User 


from .forms import CustomUserCreationForm
from .models import CustomUser
from .serializers import UserSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('recipes_list')
    serializer_class = UserSerializer
    # redirect_field_name = 'home'

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()