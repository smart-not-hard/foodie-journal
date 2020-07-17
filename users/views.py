from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from django.contrib.auth.models import User 
from rest_framework.generics import ListAPIView

from .forms import CustomUserCreationForm
from .models import CustomUser
from .serializers import UserSerializer, CustomUserSerializer 

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('recipes_list')
    serializer_class = UserSerializer
    # redirect_field_name = 'home'

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = ()

class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer