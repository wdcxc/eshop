from __future__ import unicode_literals

from django.db import models

from models.product import ProductModel


class CustomerModel(models.Model):
    """买家模型"""
    MALE = 1
    FEMALE = 2
    SECRET = 3
    SEX = ((MALE, 'male'), (FEMALE, 'female'), (SECRET, 'secret'))

    name = models.CharField(max_length=30, unique=True)  # 用户名
    password = models.CharField(max_length=150)  # 登录密码
    nickname = models.CharField(max_length=30, null=True)  # 昵称
    truename = models.CharField(max_length=30, null=True)  # 真实姓名
    mobile = models.CharField(max_length=15, unique=True, null=True)  # 手机
    email = models.CharField(max_length=30, unique=True, null=True)  # 邮箱
    avatar = models.URLField()  # 买家头像
    registTime = models.DateTimeField(auto_now_add=True)  # 注册时间
    birthday = models.DateField(null=True)  # 生日
    sex = models.IntegerField(choices=SEX, default=SECRET)  # 性别
    level = models.IntegerField(default=0)  # 等级

    class Meta:
        db_table = "customer"


class ReceiveAddressModel(models.Model):
    """收件地址模型"""
    address = models.CharField(max_length=100)  # 收件地址
    mobile = models.CharField(max_length=15)  # 收件人手机
    name = models.CharField(max_length=30)  # 收件人姓名
    default = models.BooleanField(default=False)  # 是否为默认地址
    province = models.CharField(max_length=20, default="")  # 省份
    city = models.CharField(max_length=20, default="")  # 城市
    dist = models.CharField(max_length=20, default="")  # 区
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name="receiveAddresses")
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer_receiveaddress"


class ShopcartModel(models.Model):
    """购物车模型"""
    customer = models.ForeignKey(CustomerModel, related_name="shopcarts", on_delete=models.CASCADE)  # 归属买家
    product = models.ForeignKey(ProductModel, related_name="shopcarts", on_delete=models.CASCADE)  # 商品
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer_shopcart"


class CollectionModel(models.Model):
    """买家收藏模型"""
    customer = models.ForeignKey(CustomerModel, related_name="collections", on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, related_name="collections", on_delete=models.CASCADE)
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer_collection"


class ProductConsultModel(models.Model):
    """商品咨询模型"""

    question = models.CharField(max_length=100)  # 问题
    answer = models.CharField(max_length=100)  # 回复
    customer = models.ForeignKey(CustomerModel, related_name="consults", on_delete=models.CASCADE)  # 买家
    product = models.ForeignKey(ProductModel, related_name="consults", on_delete=models.CASCADE)  #
    askTime = models.DateTimeField()  # 提问时间
    replyTime = models.DateTimeField()  # 回复时间

    class Meta:
        db_table = "product_consult"
