# -*- coding:utf-8 -*-

from rest_framework import serializers
from test_user.models import UserInfo, LANGUAGE_CHOICES, STYLE_CHOICES


class UserInfoSerializer(serializers.Serializer):                # 它序列化的方式很类似于Django的forms
    id = serializers.IntegerField(read_only=True)
    umobile = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=20)
    uname = serializers.CharField(max_length=18, default='')  # user name
    unickname = serializers.CharField(max_length=20, default='')  # user nick name
    uage = serializers.IntegerField(default=0)  # user age
    usex = serializers.CharField(max_length=5,default='男')  # True male  False female
   # uheadimg = serializers.ImageField('头像', null=True)  # user image


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UserInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.umobile = validated_data.get('umobile', instance.umobile)
        instance.password = validated_data.get('password', instance.password)
        instance.uname = validated_data.get('uname', instance.password)
        instance.unickname = validated_data.get('unickname', instance.unickname)
        instance.uage = validated_data.get('uage', instance.uage)
        instance.usex = validated_data.get('usex', instance.usex)
      #  instance.uheadimg = validated_data.get('uheadimg', instance.uheadimg)
        instance.save()
        return instance

    class Meta:
        model = UserInfo
        fields = ('created', 'umobile', 'password', 'uname', 'unickname', 'uage', 'usex')


