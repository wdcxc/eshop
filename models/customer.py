from __future__ import unicode_literals

from django.db import models


class CustomerModel(models.Model):
    """买家模型"""
    name = models.CharField(max_length=30, unique=True) # 用户名
    password = models.CharField(max_length=150) # 登录密码
    mobile = models.CharField(max_length=15, unique=True, null=True) # 手机
    email = models.CharField(max_length=30, unique=True, null=True) # 邮箱
    avatar = models.URLField() # 买家头像
    registTime = models.DateTimeField(auto_now_add=True) # 注册时间

    class Meta:
        db_table = "customer"

class ReceiveAddressModel(models.Model):
    """收件地址模型"""
    address = models.CharField(max_length=100) # 收件地址
    mobile = models.CharField(max_length=15) # 收件人手机
    name = models.CharField(max_length=30) # 收件人姓名
    customer = models.ForeignKey("CustomerModel",on_delete=models.CASCADE,related_query_name="recevieAddresses",related_name="customer")
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer_receiveaddress"