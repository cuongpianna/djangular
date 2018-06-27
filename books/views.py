from django.shortcuts import render
from rest_framework import viewsets

from .models import Category,Book
from .serizalizer import CategorySerizalizer,BookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerizalizer
    queryset = Category.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()