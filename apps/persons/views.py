from django.shortcuts import render
from apps.persons.models import User
from apps.persons.models import StoreAdmin
from apps.persons.serializers import  UserSerializer
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
import re
import uuid
# Create your views here.

# #判断用户邮箱格式是否合理
# def validateEmail(email):
#     if len(email) > 7:
#         if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
#             return True
#     return False


def get_objects_by_userName(userName):
    try:
        return User.objects.filter(userName=userName)
    except User.DoesNotExist:
        raise Http404

class UserRegister(APIView):
    """
    接收普通用户注册资料，需要userName，password，nickName，并把注册结果信息返还给客户端,判断是否重复注册
    """
    def post(self,request):
        requestDict = request.data.dict()
        userName = requestDict["userName"]
        # #邮箱格式是否正确，前端工作
        # if validateEmail(userName)==False:
        #     return Response({'result':'failed','reason':'Email form is not right!'})
        #是否重复注册
        userObject = User.objects.filter(userName=userName)
        if userObject.exists():
            return Response({'result':'failed','reason':'The email has been used!'})
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, userName=userName)
        serializer = UserSerializer(user)
        responseDict = serializer.data
        responseDict['result'] = 'ok'
        return Response(responseDict)

class UserLogin(APIView):
     """
    验证用户的userName和password，如果正确就返回用户的基础信息
    """
     def get(self,request):
         # 检查参数中是否有userName和password
         requestDict = request.query_params.dict()
         userName = requestDict["userName"]
         if ('userName' in requestDict and 'password' in requestDict) == False:
             return Response({'result': 'missing userName or password'})

         userSet = get_objects_by_userName(userName)
         if userSet.exists() == False:
             responseDict = {'result': 'failed', 'reason': 'wrong userName'}
             return Response(responseDict)
         else:
             user = userSet[0]
             if requestDict['password'] == user.password:
                 if(user.uuid != ''):
                     return Response({'result': 'You can not login second!'})
                 serializer = UserSerializer(user,data=request.data)
                 uuidNumber = uuid.uuid1()
                 if serializer.is_valid():
                     serializer.validated_data['uuid'] = uuidNumber
                     serializer.save()
                 responseDict = serializer.data
                 #del (responseDict['password'])
                 responseDict['result'] = 'ok'
                 responseDict['uuid'] = uuidNumber
                 return Response(responseDict)
             else:
                 return Response({'result' : 'failed','reason' : 'wrong password'})
class UserLogout(APIView):
    """
    用户退出登录状态,需要uuid
    """
    def delete(self,request):
        requestDict = request.data.dict()
        if ('uuid' in requestDict) == False:
            return Response({'result': 'failed', 'reason': 'Please send your uuid first!'})
        userObject = get_object_or_404(User,uuid = requestDict['uuid'])
        serializer = UserSerializer(userObject,data=request.data)
        if serializer.is_valid():
            serializer.validated_data['uuid'] = ''
            serializer.save()
            return Response({'result':"You're logged out."})
        else:
            return Response({'result': 'failed', 'reason': 'Invalid data'})

class AdminLogin(APIView):
    """
    管理员登录，检查账号是否正确
    """
    def get(self,request):
        requestDict = request.query_params.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result': 'failed','reason':'you have no access permission!'})
        # 验证管理员身份
        adminObjects = StoreAdmin.objects.all()
        adminSerializer = AdminSerializer(adminObjects, many=True)
        for e in adminSerializer.data:  # 只要是管理员
            if (requestDict['adminId'] == e['adminId'] and requestDict['password'] == e['adminPassword']):
                return Response({'result':'ok'})
        return Response({'result': 'failed','reason':'you have no access permission!'})
