import django.forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#         # excludes = ()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)
UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'password1', 'password2',)
    }),
)