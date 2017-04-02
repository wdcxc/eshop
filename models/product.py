from django.db import models

from models.productcategory import ProductCategoryModel, PropertyMetaModel
from models.seller import SellerModel


class ProductModel(models.Model):
    """商品模型"""
    PRESELL = 0
    ONSHELVE = 1
    OFFSHELVE = 2
    SOLDOUT = 3
    UNCERTAIN = 4
    STATUS = ((PRESELL,"persell"),(ONSHELVE, "onshelve"), (OFFSHELVE, "offshelve"),(SOLDOUT,"soldout"),(UNCERTAIN,"uncertain"))

    status = models.IntegerField(choices=STATUS, default=PRESELL)  # 商品状态
    name = models.CharField(max_length=100)  # 商品名称
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.SET_NULL, null=True,
                                 related_name="products")  # 商品类别id
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品价格
    brand = models.CharField(max_length=50)  # 商品品牌
    amount = models.IntegerField(default=0)  # 商品在售数量
    soldoutAmount = models.IntegerField(default=0)  # 商品售出数量
    seller = models.ForeignKey(SellerModel, related_name="products", on_delete=models.CASCADE)  # 卖家
    addTime = models.DateTimeField(auto_now_add=True)  # 商品添加时间
    onShelveTime = models.DateTimeField(null=True)  # 商品上架时间
    offShelveTime = models.DateTimeField(null=True)  # 商品下架时间
    description = models.TextField(null=True)  # 商品描述

    class Meta:
        db_table = "product"


class PropertyModel(models.Model):
    """商品属性模型"""
    meta = models.ForeignKey(PropertyMetaModel, related_name="properties", on_delete=models.CASCADE)  # 属性元型
    value = models.CharField(max_length=50, default="")  # 属性值
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="properties")  # 属性归属商品

    class Meta:
        db_table = "product_property"


class ProductImageModel(models.Model):
    """商品图片"""
    name = models.CharField(max_length=20,null=True)  # 图片名称
    order = models.IntegerField(default=0)  # 显示顺序,数字越大，显示越前
    product = models.ForeignKey(ProductModel, related_name="images", on_delete=models.CASCADE)  # 关联产品
    url = models.URLField()  # 图片链接地址
    addTime = models.DateTimeField(auto_now_add=True)  # 图片添加时间

    class Meta:
        db_table = "product_image"
