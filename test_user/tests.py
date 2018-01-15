from django.test import TestCase

# Create your tests here.
from test_user.models import UserInfo
from test_user.serializers import UserInfoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


user = UserInfo(umobile='18565607772',password='285897254')
user.save()

user = UserInfo(umobile='13888888888',password='285897254')
user.save()

serializer = UserInfoSerializer(user)

serializer.data
