from django.urls import path
from .views import SignUpView
 
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='recipes_signup'),        # signup
    path('signin/', SignUpView.as_view(), name='recipes_signin'),        # signin
]