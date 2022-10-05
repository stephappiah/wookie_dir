from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class BooksAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['author'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class CRUDBook(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.serializer_class(book)
        return Response(serializer.data, status=200)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return Response(status=204)

    def patch(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.serializer_class(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
