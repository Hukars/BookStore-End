from rest_framework import serializers
from .models import ShoppingCart,ShoppingOrder,ShoppingRecord

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('id','book','user','bookNumber','totalPrice')

class ShoppingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingOrder
        fields = ('id','created_at','deliveryTime','orderState','totalMoney')

class ShoppingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingRecord
        fields = ('id','book','user','bookNumber','shoppingOrder')