from typing import OrderedDict
from rest_framework.response import Response
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import get_object_or_404
from wookie_dir.common.permissions import BookViewPermission


class BooksAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [BookViewPermission]

    def get_queryset(self):
        return Book.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset_or_object(self):
        """This method is used to get the queryset or object
            Returns queryset/object, many (True/False)
        """
        if self.kwargs.get('pk'):
            return self.get_object(), False
        return self.get_queryset(), True

    def post(self, request, *args, **kwargs):
        data = OrderedDict()
        data.update(request.data)
        data['author'] = request.user.id
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request, *args, **kwargs):
        queryset, many = self.get_queryset_or_object()
        serializer = self.serializer_class(queryset, many=many)
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
