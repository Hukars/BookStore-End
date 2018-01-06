from django.shortcuts import render
from .models import CommonProblem,SystemRule
from apps.persons.models import StoreAdmin
from .serializers import SystemRuleSerializer,CommonProblemSerializer
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

#--------帮助模块主要实现系统规则的增删改查，常见问题的增删改查

class SystemRuleList(APIView):
    """
    获取系统规则列表需求
    """
    def get(self,request):
        responseDict = []
        systemRuleSet = SystemRule.objects.all()
        for e in systemRuleSet:
            systemRuleDict = model_to_dict(e)
            responseDict.append(systemRuleDict)
        return Response({"systemRuleList":responseDict})
class DeleteRule(APIView):
    """
    管理员删除系统某项规则,需要管理员id和password
    """
    def delete(self,request,id):
        requestDict = request.data.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result': 'failed','reason':'you have no access permission!'})
        ruleObject = get_object_or_404(SystemRule,ruleId=id)
        adminObject = get_object_or_404(StoreAdmin,adminId=requestDict['adminId'])
        if adminObject.adminPassword == requestDict['password']:
            #管理员验证成功
            ruleObject.delete()
            return Response({'result': "ok"})
        return Response({'result': 'failed','reason':'your information is wrong!'})
class AddRule(APIView):
    """
    管理员添加系统规则，需要管理员id和password
    """
    def post(self,request):
        requestDict = request.data.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result': 'failed','reason':'you have no access permission!'})
        adminObject = get_object_or_404(StoreAdmin, adminId=requestDict['adminId'])
        if adminObject.adminPassword == requestDict['password']:
            # 管理员验证成功
            serializer = SystemRuleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                responseDict = {'result': "ok"}
                return Response(responseDict, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': 'failed','reason':'your information is wrong!'})
class UpdateRule(APIView):
    """
    管理员修改某个规则，需要管理员id和password
    """
    def put(self,request,id):
        requestDict = request.data.dict()
        if ('adminId' in requestDict and 'password' in requestDict) == False:
            return Response({'result': 'failed','reason':'you have no access permission!'})
        adminObject = get_object_or_404(StoreAdmin, adminId=requestDict['adminId'])
        if adminObject.adminPassword == requestDict['password']:
            # 管理员验证成功
            systemRuleObject = get_object_or_404(SystemRule,ruleId=id)
            serializer = SystemRuleSerializer(systemRuleObject,data=request.data)
            if serializer.is_valid():
                serializer.save()
                responseDict = serializer.data
                responseDict['result'] = 'ok'
                return Response(responseDict)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result': 'failed','reason':'your information is wrong!'})

class CommonProblemList(APIView):
    """
    用户获取系统常见问题列表
    """
    def get(self,request):
        resposeDict = []
        commonProblemSet = CommonProblem.objects.all()
        for e in commonProblemSet:
            commonProblemDict = model_to_dict(e)
            resposeDict.append(commonProblemDict)
        return Response({"systemRuleList": resposeDict})
