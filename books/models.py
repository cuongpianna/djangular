from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    page = models.IntegerField()
    file = models.FileField(upload_to='uploads')
    category = models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
