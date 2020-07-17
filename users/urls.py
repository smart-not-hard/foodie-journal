from django.urls import path
from .views import UserCreate, UserListView

 
urlpatterns = [

    path('register/', UserCreate.as_view()),                          # create
    path('', UserListView.as_view())
]