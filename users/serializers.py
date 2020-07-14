from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ()
        model = CustomUser
        