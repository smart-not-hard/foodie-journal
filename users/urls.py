from django.urls import path
from .views import SignUpView, UserCreate

 
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='user_signup'),        # signup
    path('signin/', SignUpView.as_view(), name='user_signin'),        # signin
    path('register/', UserCreate.as_view()),                          # create
]