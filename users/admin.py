# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# from .forms import CustomUserChangeForm, CustomUserCreationForm

# # Register your models here.


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username']

# admin.site.register(CustomUser, CustomUserAdmin)

# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .forms import UserCreationFormExtended
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationFormExtended
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)


# class UserCreationFormExtended(UserCreationForm): 
#     def __init__(self, *args, **kwargs): 
#         super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
#         self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)
# UserAdmin.add_form = UserCreationFormExtended
# UserAdmin.add_fieldsets = (
#     (None, {
#         'classes': ('wide',),
#         'fields': ('email', 'username', 'password1', 'password2',)
#     }),
# )
# admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)