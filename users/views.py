from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CustomUser
from .serializers import UserCreateSerializer, UserListSerializer


class UserCreate(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = ()

class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (ISAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer