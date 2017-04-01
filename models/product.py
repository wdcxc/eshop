from django.db import models

from models.productcategory import ProductCategoryModel, PropertyMetaModel
from models.seller import SellerModel


class ProductModel(models.Model):
    """商品模型"""
    name = models.CharField(max_length=100)  # 商品名称
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.SET_NULL, null=True,
                                 related_name="products")  # 商品类别id
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品价格
    brand = models.CharField(max_length=50)  # 商品品牌
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 商品在售数量
    soldoutAmount = models.DecimalField(max_digits=10, decimal_places=2)  # 商品售出数量
    seller = models.ForeignKey(SellerModel, related_name="products", on_delete=models.CASCADE)  # 卖家
    addTime = models.DateTimeField(auto_now_add=True)  # 商品添加时间
    onShelveTime = models.DateTimeField(null=True)  # 商品上架时间
    offShelveTime = models.DateTimeField(null=True)  # 商品下架时间
    description = models.TextField()  # 商品描述
    thumbnailLink = models.URLField()  # 商品缩略图

    class Meta:
        db_table = "product"


class Property(models.Model):
    """商品属性模型"""
    meta = models.ForeignKey(PropertyMetaModel, related_name="properties", on_delete=models.CASCADE)
    value = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "product_property"

