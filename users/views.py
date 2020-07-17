from rest_framework.generics import ListAPIView, CreateAPIView
from .models import CustomUser
from .serializers import UserCreateSerializer, UserListSerializer 


class UserCreate(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    # permission_classes = ()

class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer