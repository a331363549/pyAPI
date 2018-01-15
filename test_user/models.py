from django.db import models
from markdown import serializers
from pygments.lexers import get_all_lexers         # 一个实现代码高亮的模块
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())     # 列出所有配色风格


class UserInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    umobile = models.CharField('手机号',max_length=11)
    password = models.CharField('密码', max_length=20)
    uname = models.CharField('用户名', max_length=18, null=True, blank=True)  # user name
    unickname = models.CharField('昵称', max_length=20, null=True, blank=True)  # user nick name
    uage = models.IntegerField('年龄', null=True, blank=True)  # user age
    usex = models.CharField('性别',max_length=5, default='1')  # True male  False female
    #uheadimg = models.ImageField('头像', null=True, blank=True)  # user image


    class Meta:
        ordering = ('created',)

