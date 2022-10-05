from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelField):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')
