from __future__ import unicode_literals

from django.db import models

class CarouselModel(models.Model):
    """首页轮播页"""
    class Meta:
        db_table = "index_carousel"

    title = models.CharField(max_length=50) # 标题
    show = models.BooleanField(default=True) # 是否显示
    order = models.IntegerField(default=1) # 展示权重（权重越大，展示越前）
    imgUrl = models.URLField() # 图片链接地址
    linkUrl = models.URLField() # 点击跳转链接
    addTime = models.DateTimeField(auto_now_add=True)

class ProductCategoryModel(models.Model):
    """商品类别目录"""
    class Meta:
        db_table = "product_category"

    def __str__(self):
        return "{id}:{name}".format(id=self.id,name=self.name)

    parentId = models.IntegerField(default=0) # 父类别（0:根节点）
    name = models.CharField(max_length=100) # 类别名称
    order = models.IntegerField(default=1) # 显示权重（用于同一父类下子节点比较，权重越大，显示越前）
    grade = models.IntegerField(default=1) # 节点等级（等级越低，级别越高，1:顶级节点）
    show = models.BooleanField(default=True) # 是否显示
    addTime = models.DateTimeField(auto_now_add=True) # 添加时间




