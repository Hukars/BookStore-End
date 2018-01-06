from django.db import models

# Create your models here.

class Book(models.Model):
    bookName = models.CharField(max_length=50,default="")
    bookAuthor = models.CharField(max_length=30,default="")
    bookISBN = models.CharField(max_length=50,default='')
    bookType = models.CharField(max_length=30,default="计算机科学")
    bookPress = models.CharField(max_length=50,default="")
    bookPublishDate = models.CharField(max_length=50,default='')#1998-1-23格式
    bookPrice = models.FloatField(default=100.0)
    bookNumbers = models.IntegerField(default=1)
    bookImageUrl = models.URLField(max_length=500,default="")
    bookAuthorIntroduction = models.TextField(max_length=500,default="")
    bookIntroduction = models.TextField(max_length=500,default="")