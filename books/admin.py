from django.contrib import admin
from .models import Book,Category

admin.site.register(Category)
admin.site.register(Book)