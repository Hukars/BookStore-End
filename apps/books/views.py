from django.shortcuts import render
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from apps.persons.models import StoreAdmin
from apps.persons.serializers import AdminSerializer
from django.forms.models import model_to_dict
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework import request
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

# Create your views here.
def splitPictureURL(image_url):
    """
    以逗号为分隔符切割图片URL，转化为一个数组
    """
    images = image_url.split(',')
    return images

#----------总体实现图书的增、删、改、查，其中增删改只面向管理员

class BookList(APIView):
    """
    获取所有书籍列表需求
    """
    def get(self,request):
        bookObjectSet = Book.objects.all()
        responseDict = []
        for e in bookObjectSet:
            bookObjectDict = model_to_dict(e)
            bookObjectDict['bookImageUrl'] = splitPictureURL(bookObjectDict['bookImageUrl'])
            responseDict.append(bookObjectDict)
        return Response({'books':responseDict})

class BookDetail(APIView):
    """
    处理用户获取图书详情的请求
    """
    def get(self, request, id):
        bookObject = get_object_or_404(Book, id=id)
        responseDict = model_to_dict(bookObject)

        #对响应给用户的球场信息进行处理
        responseDict['bookImageUrl'] = splitPictureURL(responseDict['bookImageUrl'])
        return Response(responseDict)

class BookSearch(APIView):
      """
      查询书籍，根据书籍名，作者，图书类型顺序模糊查询,返回Book List
      """
      def get(self, request):
          requestDict = request.query_params.dict()
          responseDict = []

        #处理用户查询球场的请求
          if 'bookName' in requestDict:
             bookObjects = Book.objects.filter(bookName__contains=requestDict['bookName'])
             bookSerializer = BookSerializer(bookObjects, many=True)
             for e in bookSerializer.data:
                 e['bookImageUrl'] = splitPictureURL(e['bookImageUrl'])
                 responseDict.append(e)
             return Response({'books': responseDict})

          if 'bookAuthor'in requestDict:
              bookObjects = Book.objects.filter(bookAuthor__contains=requestDict['bookAuthor'])
              bookSerializer = BookSerializer(bookObjects, many=True)
              for e in bookSerializer.data:
                  e['bookImageUrl'] = splitPictureURL(e['bookImageUrl'])
                  responseDict.append(e)
              return Response({'books': responseDict})

          if 'bookType'in requestDict:
              bookObjects = Book.objects.filter(bookType=requestDict['bookType'])
              bookSerializer = BookSerializer(bookObjects, many=True)
              for e in bookSerializer.data:
                  e['bookImageUrl'] = splitPictureURL(e['bookImageUrl'])
                  responseDict.append(e)
              return Response({'books': responseDict})

          return Response({'books':'no results'})

class BookCreation(APIView):
    """
    往数据库中添加书籍的接口,需管理员账号方可执行
    """
    def post(self, request):
        #检查参数中是否有admin和password
        requestDict = request.data.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result': 'failed','reason': 'you have no access permission!'})
        #验证管理员身份
        adminObjects = StoreAdmin.objects.all()
        adminSerializer = AdminSerializer(adminObjects,many=True)
        for e in adminSerializer.data:#只要是管理员
            if (requestDict['adminId'] == e['adminId'] and requestDict['password'] == e['adminPassword'] ):
                # 将书籍信息存入数据库
                serializer = BookSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    responseDict = {'result': "ok"}
                    return Response(responseDict, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': 'failed','reason':'your information is wrong!'})

class BookUpdate(APIView):
    """
    更新书籍信息接口,需管理员账号和书籍id方可执行
    """
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        serializer = BookSerializer(book)
        responseDict = serializer.data
        return Response(responseDict)

    def put(self, request, id):
        # 检查参数中是否有管理员账号
        requestDict = request.data.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result': 'failed','reason': 'you have no access permission'})
        book = get_object_or_404(Book,id=id)

        # 验证管理员身份
        adminObjects = StoreAdmin.objects.all()
        adminSerializer = AdminSerializer(adminObjects, many=True)

        for e in adminSerializer.data:  # 只要是管理员
            if (requestDict['adminId'] == e['adminId'] and requestDict['password'] == e['adminPassword']):
                # 将管理员修改的图书信息存入数据库
                serializer = BookSerializer(book, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    responseDict = serializer.data
                    responseDict['result'] = 'ok'
                    return Response(responseDict)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result': 'failed','reason':'your information is wrong!'})

class BookDelete(APIView):
    """
    删除接口,需管理员账号和书籍id方可执行
    """
    def delete(self,request,id):
        requestDict = request.data.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result': 'failed', 'reason': 'you have no access permission'})
        book = get_object_or_404(Book, id=id)

        # 验证管理员身份
        adminObjects = StoreAdmin.objects.all()
        adminSerializer = AdminSerializer(adminObjects, many=True)

        for e in adminSerializer.data:  # 只要是管理员
            if (requestDict['adminId'] == e['adminId'] and requestDict['password'] == e['adminPassword']):
                # 将管理员修改的图书信息存入数据库
                book.delete()
                return Response({'result': "ok"})
        return Response({'result': 'failed', 'reason': 'your information is wrong!'})