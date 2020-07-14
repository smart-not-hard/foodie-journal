from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm
from .models import CustomUser
from .serializers import UserSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('recipes_list')
    serializer_class = UserSerializer
    
    # redirect_field_name = 'home'

