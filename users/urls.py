from django.urls import path
from .views import UserCreate, UserListView, UserDetail

 
urlpatterns = [

    path('register/', UserCreate.as_view()),                          # create
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetail.as_view(),)
]