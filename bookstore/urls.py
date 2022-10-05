from django.contrib import admin
from django.urls import path
from .views import BooksAPIView

urlpatterns = [
    path('', BooksAPIView.as_view(), name='books'),
    path('<int:pk>/', BooksAPIView.as_view(), name='books'),
]
