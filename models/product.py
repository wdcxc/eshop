from django.db import models


class Product(models.Model):
    """商品"""
    name = models.CharField(max_length=100)  # 商品名称
    category = models.ForeignKey('ProductCategoryModel', on_delete=models.SET_NULL, null=True,
                                 related_name="category", related_query_name="products")  # 商品类别id
    price = models.DecimalField()  # 商品价格
    brand = models.CharField(max_length=50)  # 商品品牌
    amount = models.DecimalField()  # 商品在售数量
    soldoutAmount = models.DecimalField()  # 商品售出数量
    sellerId = models.IntegerField()  # 出售商品商铺id
    addTime = models.DateTimeField(auto_now_add=True)  # 商品添加时间
    onShelveTime = models.DateTimeField()  # 商品上架时间
    offShelveTime = models.DateTimeField()  # 商品下架时间
    description = models.TextField()  # 商品描述
    thumbnailLink = models.URLField()  # 商品缩略图

    class Meta:
        db_table = "product"
