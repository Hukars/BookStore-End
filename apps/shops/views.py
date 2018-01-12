from django.shortcuts import render
from apps.books.models import Book
from apps.persons.models import User, StoreAdmin
from .models import ShoppingCart,ShoppingRecord,ShoppingOrder
from .serializers import ShoppingCartSerializer,ShoppingOrderSerializer,ShoppingRecordSerializer
from django.forms.models import model_to_dict
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework import request
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
import time
import re
# Create your views here.

#----------用户购物车：计划实现操作：加入购物车，删除出购物车,获取购物车List
class ShoppingCartList(APIView):
    """
    处理用户获取购物车所有条目的请求，需要用户登录状态，返回书和书的一些相关信息
    """
    def get(self,request):
        #requestDict = request.query_params.dict()
        if ("member_id"  in  request.session)==False:
            return Response({'result':'failed','reason': 'Please log in first!'})
        userName = request.session['member_id']

        # 通过用户名获取所有条目
        userObject = get_object_or_404(User,userName = userName)
        shoppingCartList = ShoppingCart.objects.filter(user=userObject)
        #处理对象集
        resposeDict = []
        for e in shoppingCartList:
            shoppingCartDict = model_to_dict(e)
            resposeDict.append(shoppingCartDict)
        return Response({'shoppingCartList':resposeDict})

class AddCart(APIView):
    """
    处理用户加入购物车请求,需要用户登录是登录状态，并提供bookId，bookNumber属性
    """
    def post(self,request):
        #检查请求字段是否有userName，bookID和bookNumber
        requestDict = request.data.dict()
        if('bookId' in requestDict and 'bookNumber' in requestDict)==False:
            return Response({'result':'failed','reason': 'missing bookId or bookNumber'})

        # 通过cookie验证用户是否登录
        if ("member_id" in request.session) == False:
            return Response({'result':'failed','reason': 'Please log in first!'})
        userName = request.session['member_id']

        userObject = get_object_or_404(User,userName = userName)
        bookObject = get_object_or_404(Book,id = requestDict['bookId'])
        #如果用户强行加入比库存还多的书，返回错误信息
        if int(requestDict['bookNumber']) > bookObject.bookNumbers:
            return Response({'result':'failed','reason':'The stock is not enough,please decrease you number'})
        #检查是否存在是同一件同一个用户购物车的图书，如果是，只需修改数量和价格
        shoppingCartSet = ShoppingCart.objects.filter(book=bookObject,user=userObject)
        if shoppingCartSet.exists():
            shoppingCartObject = shoppingCartSet[0]
            shoppingCartObject.bookNumber += int(requestDict['bookNumber'])
            shoppingCartObject.totalPrice += (float)(requestDict['bookNumber']) * shoppingCartObject.singlePrice
            shoppingCartObject.save()
            return Response({'result': 'ok'})
        # 如果不是，创建购物车的一个新条目
        shoppingCartSerializer = ShoppingCartSerializer(data=request.data)
        if shoppingCartSerializer.is_valid():
            shoppingCartSerializer.validated_data['book'] = bookObject
            shoppingCartSerializer.validated_data['user'] = userObject
            shoppingCartSerializer.validated_data['singlePrice'] = bookObject.bookPrice
            shoppingCartSerializer.validated_data['totalPrice'] = bookObject.bookPrice * (float)(requestDict['bookNumber'])
            shoppingCartSerializer.save()
            return Response({'result':'ok'})
        else:
            return Response(shoppingCartSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCart(APIView):
    '''
    处理用户删除购物车一个条目的请求，需要用户登录状态和条目的id
    '''
    def delete(self,request,id):
        requestDict = request.data.dict()
        # 通过cookie验证用户是否登录
        if ("member_id" in request.session) == False:
            return Response({'result': 'failed', 'reason': 'Please log in first!'})
        userName = request.session['member_id']
        #获取条目，并验证用户名
        shoppingCartObject = get_object_or_404(ShoppingCart,id=id)
        shoppingCartSerializer = ShoppingCartSerializer(data=model_to_dict(shoppingCartObject))
        userObject = get_object_or_404(User,userName = userName)
        if shoppingCartSerializer.is_valid():
            if(userObject == shoppingCartSerializer.validated_data['user']):
                shoppingCartObject.delete()
                return Response({'result':'ok'})
            else:
                return Response({'result':'failed','reason':'your userName can not delete this item!!'})
        return Response(shoppingCartSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpdateCart(APIView):
    """
    处理用户修改购物车一个条目的请求，在这里特指想买书的数量,需要用户登录状态和条目的id和bookNumber
    """
    def put(self,request,id):
        requestDict = request.data.dict()
        # 判断是否有bookNumber
        if ('bookNumber' in requestDict) == False:
            return Response({'result':'failed','reason': 'missing bookNumber'})
        if len(requestDict)>1:
            return Response({'result':'failed','reason': 'You can only update the number of books'})

        # 通过cookie验证用户是否登录
        if ("member_id" in request.session) == False:
            return Response({'result': 'failed', 'reason': 'Please log in first!'})
        userName = request.session['member_id']

        # 获取条目，并验证用户名
        shoppingCartObject = get_object_or_404(ShoppingCart, id=id)
        singlePrice = shoppingCartObject.totalPrice/shoppingCartObject.bookNumber
        shoppingCartSerializer = ShoppingCartSerializer(shoppingCartObject, data=request.data)
        userObject = get_object_or_404(User, userName=userName)
        if shoppingCartSerializer.is_valid():
            if (userObject == shoppingCartObject.user):
                shoppingCartSerializer.validated_data['totalPrice'] = singlePrice* (float)(requestDict['bookNumber'])
                shoppingCartSerializer.save()
                responseDict = shoppingCartSerializer.data
                responseDict['result'] = 'ok'
                return Response(responseDict)
            return Response({'result':'failed','reason': 'your infomation is wrong'})
        return Response(shoppingCartSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-------------------系统订单，主要实现支付这一块功能，包括生成订单，还没有发货订单的删除，查看订单和订单的更新

def getOrderFromRecord(shoppingRecordSet):#根据购物记录找出所有的订单
    shoppingOrderSet = []
    for e in shoppingRecordSet:
        if e.shoppingOrder not in shoppingOrderSet:
            shoppingOrderSet.append(e.shoppingOrder)
    return shoppingOrderSet

class OrderList(APIView):
    """
    用户查看订单列表，需要用户登录状态
    """
    def get(self,request):
        responseDict = []
        # 通过cookie验证用户是否登录
        if ("member_id" in request.session) == False:
            return Response({'result': 'failed', 'reason': 'Please log in first!'})
        userName = request.session['member_id']
        userObject = get_object_or_404(User, userName=userName)

        # 通过用户获取购物记录和订单
        shoppingRecordSet = ShoppingRecord.objects.filter(user=userObject)
        shoppingOrderSet = []
        # 获取订单号
        if shoppingRecordSet.exists():
            shoppingOrderSet = getOrderFromRecord(shoppingRecordSet)
        else:
            return Response({'result':'failed','reason': 'you dont have any order'})
        #返回订单信息
        for e in shoppingOrderSet:
            shoppingOrderDict = model_to_dict(e)
            responseDict.append(shoppingOrderDict)
        return Response({"shoppingOrderList":responseDict})
class RecordList(APIView):
    """
    用户查看某个订单的购物记录List，需要用户登录状态和订单id
    """
    def get(self,request,id):
        # 通过cookie验证用户是否登录
        if ("member_id" in request.session) == False:
            return Response({'result': 'failed', 'reason': 'Please log in first!'})
        userName = request.session['member_id']

        userObject = get_object_or_404(User, userName=userName)
        shoppingOrderObject = get_object_or_404(ShoppingOrder,id=id)
        shoppingRecordSet = ShoppingRecord.objects.filter(shoppingOrder=shoppingOrderObject)
        # 返回订单号为id的购物记录信息
        responseDict = []
        for e in shoppingRecordSet:
            if(e.user == userObject):
                shoppingRecordDict = model_to_dict(e)
            responseDict.append(shoppingRecordDict)
        return Response({"shoppingRecordList": responseDict})


class AddOrder(APIView):
    """
    用户支付环节，生成一条订单记录和若干购买记录，需要用户登录状态，以及提供totalMoney,created_at以及选择支付的每个购物车条目的ids
    """
    def post(self,request):
        requestDict = request.data.dict()
        if('totalMoney' in requestDict and 'created_at' in requestDict and  'ids' in requestDict) == False:
            return Response({'result':'failed','reason': 'missing totalMoney,created_at or ids'})
        # 通过cookie验证用户是否登录
        if ("member_id" in request.session) == False:
            return Response({'result': 'failed', 'reason': 'Please log in first!'})
        userName = request.session['member_id']
        userObject = get_object_or_404(User, userName=userName)
        #钱不够
        if(userObject.remainder < float(requestDict['totalMoney'])):
            return Response({'result':'failed','reason': 'remainde is not enough!'})
        else:
            userObject.remainder = userObject.remainder - float(requestDict['totalMoney'])
        #生成用户订单
        shoppingOrderSerializer = ShoppingOrderSerializer(data=request.data)
        orderId = 0
        if shoppingOrderSerializer.is_valid():
            shoppingOrderSerializer.save()
            shoppingOrderObjects = ShoppingOrder.objects.filter(created_at=requestDict['created_at'],totalMoney=requestDict['totalMoney'])
            if len(shoppingOrderObjects)>1:
                for e in shoppingOrderObjects:
                    e.delete()
                print(len(shoppingOrderObjects))
            else:
                objects = shoppingOrderObjects[0]
                orderId = objects.id
        else:
            return Response(shoppingOrderSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #订单生成成功之后还需生成用户购物记录
        cartItemsIds = requestDict['ids']
        for e in cartItemsIds:
            print(e)
            cartObject = get_object_or_404(ShoppingCart,id=(int)(e))
            cartObjectDict = model_to_dict(cartObject)
            del cartObjectDict['singlePrice']
            del cartObjectDict['totalPrice']
            #减少图书数量
            bookObject = cartObject.book
            bookObject.bookNumbers = bookObject.bookNumbers - cartObject.bookNumber
            bookObject.save()
            #删除购物车条目记录
            orderObject = get_object_or_404(ShoppingOrder,id=orderId)
            shoppingRecordSerializer = ShoppingRecordSerializer(data=cartObjectDict)
            cartObject.delete()
            if shoppingRecordSerializer.is_valid():
                shoppingRecordSerializer.validated_data['shoppingOrder'] = orderObject
                shoppingRecordSerializer.save()
            else:
                return Response(shoppingOrderSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result':'ok'})
class AllOrders(APIView):
    """
    管理员查看所有订单，按时间顺序先后返回，需要管理员id和password
    """
    def get(self,request):
        responseDict = []
        requestDict = request.query_params.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result':'failed','reason': 'missing id or password'})
        adminObject = get_object_or_404(StoreAdmin, adminId=requestDict['adminId'])
        if adminObject.adminPassword == requestDict['password']:
            shoppingOrderSet = ShoppingOrder.objects.all()
            for e in shoppingOrderSet:
                shoppingOrderDict = model_to_dict(e)
                responseDict.append(shoppingOrderDict)
            return Response({'allOrders':responseDict})
        return Response({'result':'failed','reason': 'your infomation is wrong'})


class UpdateOrder(APIView):
    """
    管理员更新订单状态，需要管理员id和password和订单id号,只可以修改一次deliveryTime
    """
    def put(self,request,id):
        requestDict = request.data.dict()
        if ('adminId' in requestDict and 'password' in requestDict and 'deliveryTime' in requestDict)==False:
            return Response({'result':'failed','reason':'missing id or password or deliveryTime'})
        shoppingOrderObject = get_object_or_404(ShoppingOrder,id=id)
        adminObject = get_object_or_404(StoreAdmin, adminId=requestDict['adminId'])
        if adminObject.adminPassword != requestDict['password']:
            return Response({'result':'failed','reason': 'your infomation is wrong'})
        #判断是否已经发货过
        if shoppingOrderObject.orderState == 1:
            return Response({'result':'failed','reason':'Sorry,this order has been processed!'})
        else:
            serializer = ShoppingOrderSerializer(shoppingOrderObject,data=request.data)
            if serializer.is_valid():
                serializer.validated_data['orderState'] = 1
                serializer.save()
                return Response({'result':'ok'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteOrder(APIView):
    """
    用户删除还没有发货订单，需要用户登录状态和订单的id
    """
    def delete(self,request,id):
        # 通过cookie验证用户是否登录
        if ("member_id" in request.session) == False:
            return Response({'result': 'failed', 'reason': 'Please log in first!'})
        userName = request.session['member_id']
        userObject = get_object_or_404(User, userName=userName)
        #获取订单
        shoppingOrderObject = get_object_or_404(ShoppingOrder,id=id)
        #检验是否发货
        if (shoppingOrderObject.orderState == 1):
            return Response({'result':'failed','reason':'The order has been shipped!'})
        else:
            shoppingRecordSet = ShoppingRecord.objects.filter(shoppingOrder=shoppingOrderObject)
            if (userObject == shoppingRecordSet[0].user):
                userObject.remainder += shoppingOrderObject.totalMoney
                shoppingOrderObject.delete()
                for e in shoppingRecordSet:
                    e.delete()
                return Response({'result':'ok'})
            else:
                return Response({'result':'failed','reason':'you have no right to delete the order!'})