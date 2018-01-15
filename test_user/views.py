import re

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO

from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from test_user.models import UserInfo
from test_user.serializers import UserInfoSerializer

r = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')

def reparse():
    stream = BytesIO(content)
    data = JSONParser().parse(stream)
    serializer = UserInfoSerializer(data=data)
    serializer.is_valid()  # 开始验证
    # True
    serializer.validated_data
    serializer.save()


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
        if data['password'] != data['pw2']:
            return JsonResponse('两次输入的密码不一致', safe=False, status=400)
        else:
            user = UserInfo(umobile=data['umobile'], password=data['password'])
            #user.save()
            serializer = UserInfoSerializer(user)
            return JsonResponse('创建成功', serializer, status=201)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        post = request.POST
        umobile = post.get('umobile')
        upwd = post.get('upwd')
        users = UserInfo.objects.filter(umobile=umobile)
        if len(users) == 1:
            if upwd == users[0].password:
                users
                return JsonResponse('登录成功', status=201)
            else:
                return JsonResponse('密码错误', status=400)
        else:
            return JsonResponse('账号不存在', status=400)


@csrf_exempt
def update_info(request):
    if request.method == 'POST':
        pass


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
