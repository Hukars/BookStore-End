from django.db import models
from apps.books.models import Book
# Create your models here.
class ShoppingCart(models.Model):
    book = models.ForeignKey('books.Book',on_delete=models.CASCADE, related_name='shoppingCart_book', default='')
    user = models.ForeignKey('persons.User',on_delete=models.CASCADE,related_name='user_shoppingCart',default='')
    singlePrice = models.FloatField(default=0.0)
    bookNumber = models.IntegerField(default=0)#同一本书可能买多本
    totalPrice = models.FloatField(default=0.0)

class ShoppingOrder(models.Model):#订单
    created_at = models.CharField(max_length=100,default='')#时间格式前端发送的时间精确到秒
    deliveryTime = models.CharField(max_length=100,default='')
    orderState = models.IntegerField(default=0)#0未发货，1发货
    totalMoney = models.FloatField(default=0.0)#订单总额


class ShoppingRecord(models.Model):#购物记录
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='shoppingRecord_book', default='')
    user = models.ForeignKey('persons.User', on_delete=models.CASCADE, related_name='user_shoppingRecord', default='')
    bookNumber = models.IntegerField(default=0)  # 同一本书可能买多本
    shoppingOrder =  models.ForeignKey('shops.ShoppingOrder', on_delete=models.CASCADE, related_name='shopppingOrder_shoppingRecord', default='')