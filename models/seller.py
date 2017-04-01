from __future__ import unicode_literals

from django.db import models


class SellerModel(models.Model):
    """卖家模型"""
    name = models.CharField(max_length=30, unique=True) # 用户名
    password = models.CharField(max_length=150) # 登录密码
    mobile = models.CharField(max_length=11, unique=True, null=True) # 手机
    email = models.CharField(max_length=30, unique=True, null=True) # 邮箱
    truename = models.CharField(max_length=30) # 真实姓名
    idno = models.CharField(max_length=18,unique=True) # 身份证号码
    registTime = models.DateTimeField(auto_now_add=True) # 注册时间
    shopName = models.CharField(max_length=30,unique=True) # 店铺名
    shopAddress = models.CharField(max_length=100,null=True) # 店铺地址
    thumbnail = models.URLField(null=True) # 卖家头像

    class Meta:
        db_table = "seller"
