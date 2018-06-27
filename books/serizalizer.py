from rest_framework import serializers

from .models import Category,Book

class CategorySerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Book
        fields = ('title','author','timestamp','page','file','category')