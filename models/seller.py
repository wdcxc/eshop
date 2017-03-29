from __future__ import unicode_literals

from django.db import models


class SellerModel(models.Model):
    """卖家模型"""
    name = models.CharField(max_length=30, unique=True) # 用户名
    password = models.CharField(max_length=130) # 登录密码
    mobile = models.CharField(max_length=11, unique=True, null=True) # 手机
    email = models.CharField(max_length=30, unique=True, null=True) # 邮箱
    realname = models.CharField(max_length=30) # 真实姓名
    id = models.CharField(max_length=20,unique=True) # 身份证号码

    class Meta:
        db_table = "seller"
