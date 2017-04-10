from __future__ import unicode_literals

from django.db import models


class SellerModel(models.Model):
    """卖家模型"""
    name = models.CharField(max_length=30, unique=True)  # 用户名
    password = models.CharField(max_length=150)  # 登录密码
    mobile = models.CharField(max_length=11, unique=True, null=True)  # 手机
    email = models.CharField(max_length=30, unique=True, null=True)  # 邮箱
    truename = models.CharField(max_length=30)  # 真实姓名
    idno = models.CharField(max_length=18, unique=True)  # 身份证号码
    registTime = models.DateTimeField(auto_now_add=True)  # 注册时间
    shopName = models.CharField(max_length=30, default="")  # 店铺名
    shopAddress = models.CharField(max_length=100, default="")  # 店铺地址
    thumbnail = models.URLField(null=True)  # 卖家头像
    lockTime = models.DateTimeField(null=True)  # 账号时间
    lockReason = models.TextField(null=True)  # 账号锁定理由
    lock = models.BooleanField(default=False)  # 账号是否锁定

    class Meta:
        db_table = "seller"
