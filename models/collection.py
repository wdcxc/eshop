from django.db import models

from models.customer import CustomerModel
from models.product import ProductModel


class CollectionModel(models.Model):
    """买家收藏模型"""
    customer = models.ForeignKey(CustomerModel, related_name="collections", on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, related_name="collections", on_delete=models.CASCADE)
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer_collection"
