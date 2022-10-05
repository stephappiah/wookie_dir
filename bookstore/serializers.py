from rest_framework import serializers
from .models import Book
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    author = UserSerializer()
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, required=True)
    cover = serializers.ImageField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
