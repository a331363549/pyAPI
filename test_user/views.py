# -*- coding:utf-8 -*-

import re

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO

from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from test_user.models import UserInfo, TestData
from test_user.serializers import UserInfoSerializer, TestDataSerializer

r = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')


def reparse():
    # stream = BytesIO(content)
    data = JSONParser().parse(stream)
    serializer = UserInfoSerializer(data=data)
    serializer.is_valid()  # 开始验证
    # True
    serializer.validated_data
    serializer.save()


'''创建用户'''
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = UserInfo.objects.filter(umobile=data['umobile'])
        if len(user) == 1:
            return JsonResponse('用户已存在', safe=False, status=400)
        if not r.match(data['umobile']):
            return JsonResponse('输入正确的手机号', safe=False, status=400)
        if len(data['password']) < 6:
            return JsonResponse('密码长度不得小于6位', safe=False, status=400)
        else:
            serializer = UserInfoSerializer(data=data)
            if serializer.is_valid():
                serializer.create(data)
            return JsonResponse(serializer.data, status=201, safe=False)


'''用户登录'''
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = UserInfo.objects.filter(umobile=data['umobile'])
        if len(user) == 1:
            if data['password'] == user[0].password:
                serializer = UserInfoSerializer(data=data)
                if serializer.is_valid():
                    return JsonResponse(serializer.data, status=200, safe=False)
            else:
                return JsonResponse('密码错误', status=400, safe=False)
        else:
            return JsonResponse('账号不存在', status=400, safe=False)


'''提交信息'''
@csrf_exempt
def update_info(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = UserInfo.objects.get(umobile=data['umobile'])
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse('error', status=400, safe=False)
    else:
        return JsonResponse('账号不存在', status=400, safe=False)


'''上传检查结果'''
@csrf_exempt
def upload_data(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            UserInfo.objects.get(umobile=data['ts_umobile'])
            serializer = TestDataSerializer(data=data)
            if serializer.is_valid():
                serializer.create(data)
                return JsonResponse(serializer.data, status=200, safe=False)
        except UserInfo.DoesNotExist:
            return JsonResponse('用户不存在', status=400, safe=False)


'''查询检查数据'''
@csrf_exempt
def show_data(request,pk):
    try:
        user = UserInfo.objects.get(pk=pk)
    except UserInfo.DoesNotExist:
        return HttpResponse(status=404)

    users = TestData.objects.filter(ts_umobile=pk)
    if len(users) > 0:
        if request.method == 'GET':
            serializer = TestDataSerializer(users, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)

        if request.method == 'POST':
            serializer = TestDataSerializer(users, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)
    else:
        return JsonResponse('您还没有进行过测试', status=200, safe=False)

'''查询用户列表'''
@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


'''查询用户具体信息'''
@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = UserInfo.objects.get(pk=pk)
    except UserInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserInfoSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserInfoSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
