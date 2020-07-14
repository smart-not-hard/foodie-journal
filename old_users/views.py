# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm
from .models import CustomUser



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('recipes_list')
    # redirect_field_name = 'home'

