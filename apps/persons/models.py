from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=30,default="",primary_key=True)#connect the email
    password = models.CharField(max_length=20,default="")
    nickname = models.CharField(max_length=20,default="")#firstName+lastName
    uuid = models.CharField(max_length=50,default='')
    remainder = models.FloatField(default=0.0)#账户余额

class StoreAdmin(models.Model):
    adminId = models.CharField(max_length=20,primary_key=True)
    adminPassword = models.CharField(max_length=20,default="")
    adminEmail = models.TextField(max_length=50,default="1974921044@qq.com")
