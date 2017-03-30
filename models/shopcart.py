from django.db import models

from models.customer import CustomerModel
from models.product import ProductModel


class ShopcartModel(models.Model):
    """购物车模型"""
    customer = models.ForeignKey(CustomerModel, related_name="shopcarts", on_delete=models.CASCADE) # 归属买家
    product = models.ForeignKey(ProductModel, related_name="shopcarts", on_delete=models.CASCADE) # 商品
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer_shopcart"
